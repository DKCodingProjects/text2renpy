from src.read.csv_reader import Csv_Reader
from datetime import datetime
import os

class History_Data_Handler():
    def __init__(self, date_column = 'project_id'):
        data = Csv_Reader(os.path.join('src', 'data', 'history.csv'))
        data.open()
        self.headers = data.headers
        self.date_index = self.headers.index(date_column)
        self.content = []
        while not data.is_eof:
            row = data.readpart()
            if row:
                self.content.append(row)
    
    def format_row(row_list : list) -> str:
        row_str = ''
        for i in range(0,len(row_list)):
            row_str = row_str+str(row_list[i])
            if i != len(row_list)-1:
                row_str = str(row_str)+','
        return row_str
    
    def write_history(self):
        with open(os.path.join('src', 'data', 'history.csv'), 'w', newline='') as new_project:
            new_project.write(History_Data_Handler.format_row(self.headers))
            for row in self.content:
                row_str = History_Data_Handler.format_row(row)
                new_project.write(f'\n'+row_str)
    
    def add_history(self, proj_id : int, write_file : str, read_file : str):
        self.content.insert(0, [proj_id,datetime.now(),write_file,read_file])
        self.write_history()
    
    def delete_history(self, proj_id : int):
        id_index = self.headers.index('project_id')
        i = 0
        while True:
            if self.content:
                if i > len(self.content):
                    break
                elif self.content[i][id_index] == proj_id:
                    self.content.pop(i)
                    continue
                else:
                    i += 1
            else:
                break
        self.write_history()
    
    def delete_all_history(self):
        self.content = []
        self.write_history()