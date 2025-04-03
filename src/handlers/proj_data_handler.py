from src.read.csv_reader import Csv_Reader
from .data_handler import Data_Handler
from .hist_data_handler import History_Data_Handler
from .char_data_handler import Character_Data_Handler
import os

class Project_Data_Handler(Data_Handler):
    def __init__(self):
        super().__init__(os.path.join('data', 'projects.csv'))
        self.id_index = self.headers.index('project_id')
        self.limit = 25
        self.const_headers = ['project_id','name','path','description']
    
    def _add_defaults(self, row : list, row_number : int = -1):
        # if a value requires user input, set value to None
        default_values = [None, None, None, '']
        for i in range(0,len(default_values)):
            if default_values[i] is not None:
                if not row[i]:
                    row[i] = default_values[i]
            else:
                if not row[i]:
                    raise Exception('INVALID ROW! Column \''+self.const_headers[i]+'\' on row \''+str(row_number if row_number >= 0 else 'N/A')+'\' should be set by the user! ')
        return row
    
    ### TEST ###
    def upgrade_content(self):
        class Header_Transform():
            def __init__(self, old_index : int, new_index : int):
                self.old_index = old_index
                self.new_index = new_index
        transforms : list[Header_Transform] = []
        for header in self.const_headers:
            if header in self.headers:
                transforms.append(Header_Transform(self.headers.index(header),self.const_headers.index(header)))
        new_content = []
        for i in range(0,len(self.content)):
            new_row = ['' for _ in range(len(self.const_headers))]
            for trans in transforms:
                new_row[trans.new_index] = self.content[i][trans.old_index]
            self.content[i] = self._add_defaults(new_row,i)

        self.content = new_content
        self._write()
    
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
                    raise Exception('project_id \''+curr_id+'\' is present more than once in projects.csv. All projects must have a unique project_id!')
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
        return [str(self.create_id()), proj_name, proj_dir, '']
    
    def find_project(self, proj_name : str) -> list:
        if not proj_name:
            raise Exception('EMPTY project name! All project names must be longer than 1 character!')
        row = super()._get_row('name', proj_name)
        return row

    def create_proj(self, proj_name : str, proj_path : str):
        if not proj_name:
            raise Exception('EMPTY project name! All project names must be longer than 1 character!')
        if self.find_project(proj_name):
            raise Exception('Project \''+proj_name+'\' ALREADY EXISTS. Choose a different name, or rename the old project')
        if not proj_path:
            raise Exception('EMPTY project path! All project paths must be longer than 1 character!')
        if not os.access(proj_path, os.F_OK):
            raise Exception('INVALID project path \''+proj_path+'\'! Path either doesn\'t exist, or lacks permissions to access.')
        if not Project_Data_Handler.validate_proj(proj_path):
            raise Exception('INVALID project path \''+proj_path+'\'! Path does not lead to a Ren\'Py project\'s game directory!')
        new_row = self.default_proj(proj_name, proj_path)
        self.content.append(new_row)

    def delete_proj(self, proj_name : str):
        if not self.find_project(proj_name):
            raise Exception('Project \''+proj_name+'\' DOESN\'T EXIST. Try a different name instead.')
        else:
            self._delete_row('name', proj_name)

    def rename_proj(self, proj_name : str, new_name : str):
        if not self.find_project(proj_name):
            raise Exception('Project \''+proj_name+'\' DOESN\'T EXIST. Try a different name instead.')
        else:
            self._update_row('name', proj_name, new_name)
        