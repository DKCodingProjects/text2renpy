from .data_handler import Data_Handler
import os

class Projects_DH(Data_Handler):
    def __init__(self):
        super().__init__(os.path.join('data', 'projects.csv'))
        self.id_index = self.headers.index('project_id')
        self.limit = 25

    def upgrade_projects(self):
        const_headers =  ['project_id','name','path','description']
        default_values = [ None       , None , None , ''          ] # if a value requires user input, set value to None
        self._upgrade_content(const_headers, default_values)
    
    def write_projects(self):
        if len(self.content) <= self.limit:
            self._write(self.limit)
        else:
            raise Exception(f'FILE LIMIT REACHED! File limit of '+str(self.limit)+'\' rows in projects.csv reached! Delete a project to make room for more!\n\t(You can adjust the limit in src.data_handers.projects_dh if you want!)')
    
    def create_id(self) -> int:
        taken_id = set()
        for row in self.content:
            if row[self.id_index]:
                curr_id = int(row[self.id_index])
                if curr_id not in taken_id:
                    taken_id.add(int(row[self.id_index]))
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
    
    def _default_proj(self, proj_name : str, proj_dir : str) -> list:
        return [str(self.create_id()), proj_name, proj_dir, '']
    
    def find_proj(self, proj_name : str) -> list:
        if not proj_name:
            raise Exception('EMPTY project name! All project names must be longer than 1 character!')
        row = self._find_row('name', proj_name)
        return row

    def create_proj(self, proj_name : str, proj_path : str):
        if not proj_name:
            raise Exception('EMPTY project name: All project names must be longer than 1 character!')
        if self.find_proj(proj_name):
            raise Exception('Project \''+proj_name+'\' ALREADY EXISTS: Choose a different name, or rename the old project')
        if not proj_path:
            raise Exception('EMPTY project path: All project paths must be longer than 1 character!')
        if not os.access(proj_path, os.F_OK):
            raise Exception('INVALID project path \''+proj_path+'\': Path either doesn\'t exist, or lacks permissions to access.')
        if not Projects_DH.validate_proj(proj_path):
            raise Exception('INVALID project path \''+proj_path+'\': Path does not lead to a Ren\'Py project\'s game directory!')
        new_row = self._default_proj(proj_name, proj_path)
        self._add_row(new_row)

    def delete_proj(self, proj_name : str):
        if not self.find_proj(proj_name):
            raise Warning('POTETNIAL REDUNDANT TASK: Project \''+proj_name+'\' doesn\'t exist')
        else:
            self._delete_row('name', proj_name)
    
    def remove_all(self):
        self._remove_all()

    def rename_proj(self, proj_name : str, new_name : str):
        if not self.find_proj(proj_name):
            raise Exception('PROJECT \''+proj_name+'\' DOESN\'T EXIST: Try a different name or search data instead')
        else:
            self._update_row('name', proj_name, new_name)
    
    def update_path(self, proj_name : str, new_path : str):
        if not self.find_proj(proj_name):
            raise Exception('PROJECT \''+proj_name+'\' DOESN\'T EXIST: Try a different name or search data instead')
        else:
            self._update_row('path', self.find_proj(proj_name)[self.headers.index('path')], new_path)
    
    def set_desc(self, proj_name : str, desc : str):
        if not self.find_proj(proj_name):
            raise Exception('PROJECT \''+proj_name+'\' DOESN\'T EXIST: Try a different name or search data instead')
        else:
            self._update_row('path', self.find_proj(proj_name)[self.headers.index('path')], desc)