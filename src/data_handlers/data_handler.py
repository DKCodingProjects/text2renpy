from src.read.csv_reader import Csv_Reader
import csv

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
        self._write()
    
    def _get_row(self, column_name : str, row_value : str, count : int = 1) -> list:
        row = []
        if self.content:
            column_index = self.headers.index(column_name)
            for i in range(0,len(self.content)):
                if self.content[i][column_index] == row_value:
                    row.append(self.content[i])
                    count -= 1
                    if count == 0:
                        break
        return row
    
    def _search_rows(self, column_name : str, row_value : str) -> list[list]:
        rows = self._get_row(column_name, row_value, -1)
        return rows
    
    def _search_all(self):
        return self.content

    def _delete_row(self, column_name : str, row_value : str, count : int = 1):
        if self.content:
            column_index = self.headers.index(column_name)
            pop_index = []
            pop_offset = 0
            for i in range(0,len(self.content)):
                if self.content[i][column_index] == row_value:
                    pop_index.append(i)
                    count -= 1
                    if count == 0:
                        break
                    
            if pop_index:
                for index in pop_index:
                    self.content.pop(index - pop_offset)
                    pop_offset += 1
    
    def _remove_rows(self, column_name : str, row_value : str):
        self._delete_row(column_name, row_value, -1)

    def _remove_all(self):
        self.content = []
    
    def _update_row(self, column_name : str, row_value : str, new_value : str, count : int = 1):
        if self.content:
            column_index = self.headers.index(column_name)
            for i in range(0,len(self.content)):
                if self.content[i][column_index] == row_value:
                    self.content[i][column_index] = new_value
                    count -= 1
                    if count == 0:
                        break

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
