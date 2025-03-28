from src.read.csv_reader import Csv_Reader
import os

class Project_Data_Handler():
    def __init__(self, id_column = 'project_id'):
        data = Csv_Reader(os.path.join('src', 'data', 'projects.csv'))
        data.open()
        self.headers = data.headers
        self.id_index = self.headers.index(id_column)
        self.content = []
        while not data.is_eof:
            row = data.readpart()
            if row:
                self.content.append(row)
    
    def format_row(row_list : list) -> str:
        row_str = ''
        for i in range(0,len(row_list)):
            row_str = row_str+row_list[i]
            if i != len(row_list)-1:
                row_str = row_str+','
        return row_str
    
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
        with open(os.path.join('src', 'data', 'projects.csv'), 'w', newline='') as new_project:
            new_project.write(Project_Data_Handler.format_row(self.headers))
            for row in self.content:
                row_str = Project_Data_Handler.format_row(row)
                new_project.write(f'\n'+row_str)
    
    def create_id(self) -> int:
        id_index = self.id_index
        taken_id = set()
        for i in range(0, len(self.content)):
            row = self.content[i]
            if row[id_index]:
                curr_id = int(row[id_index])
                if curr_id not in taken_id:
                    taken_id.add(int(row[id_index]))
                else:
                    raise Exception('project_id \''+curr_id+'\' is present more than once in projects.csv. All projects must have a unique proj_id!')
            else:
                raise Exception('INVALID project_id! A project\'s id must be present!')
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
            self.content.pop(project_index)
            self.write_projects()

    def rename_proj(self, proj_name : str, new_name : str):
        if not self.name_exists(proj_name):
            raise Exception('Project \''+proj_name+'\' DOESN\'T EXIST. Try a different name instead.')
        else:
            project_index = self.find_project_index('name', proj_name)
            self.content[project_index][self.headers.index('name')] = new_name
            self.write_projects()
        