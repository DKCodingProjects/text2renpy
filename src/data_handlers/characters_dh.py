from .data_handler import Data_Handler
import os

class Characters_DH(Data_Handler):
    def __init__(self):
        super().__init__(os.path.join('data', 'characters.csv'))
        self.id_index = self.headers.index('project_id')
        self.name_index = self.headers.index('abbrev_name')
        self.limit = 1000
    
    def write_characters(self):
        self._write(self.limit)
        if len(self.content) > self.limit:
            raise Warning(f'FILE LIMIT REACHED! File limit of '+str(self.limit)+'\' rows in characters.csv reached! Deleting oldest rows in history.csv...')

    def _character_exists(self, proj_id : str, abbrev_name : str):
        for row in self.content:
            if (row[self.id_index] == proj_id) and (row[self.name_index].lower() == abbrev_name.lower()):
                return True
        return False
    
    def add_character(self, proj_id : str, abbrev_name : str, full_name : str, label):
        self._add_row([proj_id,abbrev_name,full_name,label], 0)
    
    def delete_project(self, proj_id : str):
        if not self._get_row('project_id', proj_id):
            raise Exception('NONEXISTANT Project ID! There is no row with Project ID = '+str(proj_id)+' in characters.csv')
        self._delete_row('project_id', proj_id, -1)

    def _double_delete(self, column_name1 : str, row_value1 : str, column_name2 : str, row_value2 : str, count : int = 1):
        if self.content:
            column_index1 = self.headers.index(column_name1)
            column_index2 = self.headers.index(column_name2)
            pop_index = []
            pop_offset = 0
            for i in range(0,len(self.content)):
                if (self.content[i][column_index1] == row_value1) and (self.content[i][column_index2] == row_value2):
                    pop_index.append(i)
                    count -= 1
                    if count == 0:
                        break
            if pop_index:
                for index in pop_index:
                    self.content.pop(index - pop_offset)
                    pop_offset += 1

    def delete_character(self, abbrev_name : str, proj_id : str):
        if not self._character_exists(proj_id=proj_id, abbrev_name=abbrev_name):
            raise Exception('NONEXISTANT Character! There is no abbreviated character name \''+abbrev_name.lower()+'\' with Project ID = '+str(proj_id)+' in characters.csv')
        else:
            self._double_delete('project_id', proj_id, 'abbrev_name', abbrev_name)
    
    # needs proj_id to be useful; different projects can have the same labels in their code
    # def delete_label(self, label : str):
    #     if not self._get_row('first_label', label):
    #         raise Exception('NONEXISTANT label! There is no row with First Label = '+str(label)+' in characters.csv')
    #     self._double_delete('project_id', proj_id, 'first_label', label, -1)
    
    def remove_all(self):
        self._remove_all()