from src.read.csv_reader import Csv_Reader
from .data_handler import Data_Handler
from .hist_data_handler import History_Data_Handler
from .char_data_handler import Character_Data_Handler
import os

class Project_Data_Handler(Data_Handler):
    def __init__(self):
        super().__init__(os.path.join('src', 'data', 'projects.csv'))
        self.id_index = self.headers.index('project_id')
        self.limit = 25
    
    def find_project_index(self, column_name : str, value : str) -> int:
        value = value.lower()
        column_index = self.headers.index(column_name)
        project_index = 0
        for row in self.content:
            if row[column_index].lower() == value:
                break
            else:
                project_index += 1
        if project_index == len(self.content):
            project_index = -1
        return project_index
    
    def write_projects(self):
        if len(self.content) >= self.limit and self.limit > 0:
            raise Exception('FAILED WRITE in '+self.__class__.__name__+'! If written, '+self.path+' will exceed row limit of '+str(self.limit)+' stored rows!')
        super()._write(self.limit)
    
    def create_id(self) -> int:
        id_index = self.id_index
        taken_id = set()
        for row in self.content:
            if row[id_index]:
                curr_id = int(row[id_index])
                if curr_id not in taken_id:
                    taken_id.add(int(row[id_index]))
                else:
                    raise Exception('project_id \''+curr_id+'\' is present more than once in projects.csv. All projects must have a unique proj_id!')
            else:
                raise Exception('EMPTY project_id! A project\'s id must be present!')
        new_id = 0
        while True:
            new_id += 1
            if new_id not in taken_id:
                break
        return new_id
    
    def validate_proj(proj_path : str):
        head, tail = os.path.split(proj_path)
        if tail != 'game':
            return False
        elif not os.access(os.path.join(proj_path, 'gui.rpy'), os.F_OK):
            return False
        else:
            return True
    
    def default_proj(self, proj_name : str, proj_dir : str) -> list:
        return [str(self.create_id()), proj_name, proj_dir, '', '.png', 'characters.rpy']
    
    def name_exists(self, proj_name : str) -> list:
        if not proj_name:
            raise Exception('EMPTY project name! All project names must be longer than 1 character!')
        proj_name = proj_name.lower()
        name_index = self.headers.index('name')
        proj_row = []
        for i in range(0, len(self.content)):
            row = self.content[i]
            if row[name_index].lower() == proj_name:
                proj_row = row
                break
        return proj_row

    def create_proj(self, proj_name : str, proj_path : str):
        if self.name_exists(proj_name):
            raise Exception('Project \''+proj_name+'\' ALREADY EXISTS. Choose a different name, or rename the old project')
        if not proj_path:
            raise Exception('EMPTY project path! All project paths must be longer than 1 character!')
        if not os.access(proj_path, os.F_OK):
            raise Exception('INVALID project path \''+proj_path+'\'! Path either doesn\'t exist, or lacks permissions to access.')
        if not Project_Data_Handler.validate_proj(proj_path):
            raise Exception('INVALID project path \''+proj_path+'\'! Path does not lead to a Ren\'Py project\'s game directory!')
        new_row = self.default_proj(proj_name, proj_path)
        self.content.append(new_row)
        self.write_projects()

    def delete_proj(self, proj_name : str):
        if not self.name_exists(proj_name):
            raise Exception('Project \''+proj_name+'\' DOESN\'T EXIST. Try a different name instead.')
        else:
            project_index = self.find_project_index('name', proj_name)
            proj_id = self.content[project_index][self.headers.index('project_id')]
            self.content.pop(project_index)
            hist_data = History_Data_Handler()
            hist_data.delete_project(proj_id)
            char_data = Character_Data_Handler()
            char_data.delete_project(proj_id)
            self.write_projects()

    def rename_proj(self, proj_name : str, new_name : str):
        if not self.name_exists(proj_name):
            raise Exception('Project \''+proj_name+'\' DOESN\'T EXIST. Try a different name instead.')
        else:
            project_index = self.find_project_index('name', proj_name)
            self.content[project_index][self.headers.index('name')] = new_name
            self.write_projects()
        