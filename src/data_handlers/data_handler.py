from src.read.csv_reader import Csv_Reader
import os
import csv

# Change reader to read file instead of store all its information???
# add dictionary based _get_row to find rows that require multi column value matching
# add dictionary based _delete_row to delete rows that require multi column value matching
# add dictionary based _update_row to delete rows that require multi column value matching

class Data_Handler():
    def __init__(self, path : str):
        self.path = path
        data = Csv_Reader(path)
        data.open()
        self.headers = data.headers
        self.content = []
        while not data.is_eof:
            row = data.readpart()
            if row:
                self.content.append(row)
    
    def _add_upgrade_defaults(self, row : list, const_headers : list, default_values : list, row_number : int = -1):
        for i in range(0,len(default_values)):
            if default_values[i] is not None:
                if not row[i]:
                    row[i] = default_values[i]
            elif not row[i]:
                    raise Exception('INVALID ROW! Column \''+const_headers[i]+'\' on row \''+str(row_number)+'\' should be set by the user! ')
        return row
    
    def _upgrade_content(self, const_headers : list, default_values : list):
        class Header_Transform():
            def __init__(self, old_index : int, new_index : int):  
                self.old_index = old_index
                self.new_index = new_index
        transforms : list[Header_Transform] = []
        for header in const_headers:
            if header in self.headers:
                transforms.append(Header_Transform(self.headers.index(header),const_headers.index(header)))
        for i in range(0,len(self.content)):
            new_row = ['' for _ in range(len(const_headers))]
            for trans in transforms:
                if trans.old_index < len(self.content[i]):
                    new_row[trans.new_index] = self.content[i][trans.old_index]
            self.content[i] = self._add_upgrade_defaults(new_row,const_headers,default_values,i)
        self.headers = const_headers
    
    def _search(self, search_dict : dict, count : int = 1):
        indexes = []
        if self.content:
            for i in range(0,len(self.content)):
                if count == 0:
                    break
                curr_row : list = self.content[i]
                meet_cond = True
                for key in search_dict.keys():
                    if curr_row[self.headers.index(key)] != search_dict[key]:
                        meet_cond = False
                        break
                if meet_cond:
                    indexes.append(i)
                    count -= 1
        return indexes

    def _find_row(self, column_name : str, row_value : str, count : int = 1) -> list:
        row = []
        find_index = self._search({column_name : row_value}, count)
        for index in find_index:
            row.append(self.content[index])
        return row
    
    def _get_rows(self, column_name : str, row_value : str) -> list[list]:
        rows = self._find_row(column_name, row_value, -1)
        return rows
    
    def _get_all(self):
        return self.content

    def _delete_row(self, column_name : str, row_value : str, count : int = 1):
        pop_index = self._search({column_name : row_value}, count) 
        pop_offset = 0
        for index in pop_index:
            self.content.pop(index - pop_offset)
            pop_offset += 1
    
    def _remove_rows(self, column_name : str, row_value : str):
        self._delete_row(column_name, row_value, -1)

    def _remove_all(self):
        self.content = []
    
    def _update_row(self, column_name : str, row_value : str, new_value : str, count : int = 1):
        update_index = self._search({column_name : row_value}, count)
        column_index = self.headers.index(column_name)
        for index in update_index:
            self.content[index][column_index] = new_value

    def _revise_rows(self, column_name : str, row_value : str, new_value : str):
        self._update_row(column_name, row_value, new_value, -1)
    
    def _add_row(self, row : list, index : int = None):
        if index != None and index >= 0:
            self.content.insert(index, row)
        else:
            self.content.append(row)
    
    def _insert_rows(self, rows : list[list], index : int = None):
        for row in rows:
            self._add_row(row,index)
    
    def _write(self, limit : int = 0):
            with open(self.path, 'w', newline='') as write_project:
                csv_writer = csv.writer(write_project, quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(self.headers)
                write_limit = limit if limit > 0 else len(self.content)
                for row in self.content[:write_limit]:
                    csv_writer.writerow(row)
