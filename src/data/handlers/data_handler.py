from abc import ABC, abstractmethod
from src.read.csv_reader import Csv_Reader
import csv

class Data_Handler(ABC):
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
    
    @abstractmethod 
    def _upgrade_content(self, const_headers : list):
        # method to update pre-existing csv files to current format
        # take current headers and compare them to desired headers
        # if a current header matches a desired header, record its original index and its desired index
        # if a current header doesn't exist, remove it and ignore its contents
        # for each row in self.content, update row format to keep old values while adding new values where needed
        # set self.headers to const_headers
        # write the file once again
        pass
    
    def _get_row(self, column_name : str, row_value : str, only_first : bool = True) -> list:
        row = []
        if self.content:
            column_index = self.headers.index(column_name)
            for i in range(0,len(self.content)):
                if self.content[i][column_index] == row_value:
                    row.append(self.content[i])
                    if only_first:
                        break
        return row
    
    def _search_rows(self, column_name : str, row_value : str) -> list[list]:
        rows = self._get_row(column_name, row_value, False)
        return rows
    
    def _search_all(self):
        return self.content

    def _delete_row(self, column_name : str, row_value : str, only_first : bool = True):
        if self.content:
            column_index = self.headers.index(column_name)
            pop_index = []
            pop_offset = 0
            for i in range(0,len(self.content)):
                if self.content[i][column_index] == row_value:
                    pop_index.append(i)
                    if only_first:
                        break
            if pop_index:
                for index in pop_index:
                    self.content.pop(index - pop_offset)
                    pop_offset += 1
    
    def _remove_rows(self, column_name : str, row_value : str):
        self._delete_row(column_name, row_value, False)

    def _remove_all(self):
        self.content = []
    
    def _update_row(self, column_name : str, row_value : str, new_value : str, only_first : bool = True):
        if self.content:
            column_index = self.headers.index(column_name)
            for i in range(0,len(self.content)):
                if self.content[i][column_index] == row_value:
                    self.content[i][column_index] = new_value
                    if only_first:
                        break

    def _revise_rows(self, column_name : str, row_value : str, new_value : str):
        self._update_row(column_name, row_value, new_value, False)
    
    def _add_row(self, row : list, index : int = None):
        if index != None:
            self.content.insert(index, row)
        else:
            self.content.append(row)
    
    def _insert_rows(self, rows : list[list], index : int = None):
        for row in rows:
            self._add_row(row,index)
    
    def _write(self, limit : int = 0):
            with open(self.path, 'w', newline='') as new_project:
                csv_writer = csv.writer(new_project, quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(self.headers)
                write_limit = limit if limit > 0 else len(self.content)
                for row in self.content[:write_limit]:
                    csv_writer.writerow(row)
