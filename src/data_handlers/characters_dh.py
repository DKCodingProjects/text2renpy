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
            raise Exception(f'FILE LIMIT REACHED: File limit of '+str(self.limit)+'\' rows in characters.csv reached! Delete a project to add more!')

    def _character_exists(self, project_id : str, abbrev_name : str):
        found = self._search({'project_id' : project_id, 'abbrev_name' : abbrev_name})
        if found:
            return True
        return False
    
    def add_character(self, project_id : str, abbrev_name : str, full_name : str, label):
        self._add_row([project_id,abbrev_name,full_name,label], 0)
    
    def delete_project(self, project_id : str):
        if not self._find_row('project_id', project_id):
            raise Warning('REDUNDANT TASK: There is no row with Project ID = '+str(project_id)+' in characters.csv...')
        self._delete_row('project_id', project_id, -1)

    def _double_delete(self, column_name1 : str, row_value1 : str, column_name2 : str, row_value2 : str, count : int = 1):
        pop_index = self._search({column_name1 : row_value1, column_name2 : row_value2})
        pop_offset = 0
        if pop_index:
            for index in pop_index:
                self.content.pop(index - pop_offset)
                pop_offset += 1

    def delete_character(self, abbrev_name : str, project_id : str):
        if not self._character_exists(project_id, abbrev_name):
            raise Warning('REDUNDANT TASK: There is no abbreviated character name \''+abbrev_name.lower()+'\' with Project ID = '+str(project_id)+' in characters.csv...')
        else:
            self._double_delete('project_id', project_id, 'abbrev_name', abbrev_name)
    
    def remove_all(self):
        self._remove_all()