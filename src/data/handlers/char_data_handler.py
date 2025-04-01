from src.read.csv_reader import Csv_Reader
import os

class Character_Data_Handler():
    def __init__(self, date_column = 'project_id'):
        data = Csv_Reader(os.path.join('src', 'data', 'characters.csv'))
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
    
    def write_characters(self):
        with open(os.path.join('src', 'data', 'characters.csv'), 'w', newline='') as new_characters:
            new_characters.write(Character_Data_Handler.format_row(self.headers))
            for row in self.content[:1000]:
                row_str = Character_Data_Handler.format_row(row)
                new_characters.write(f'\n'+row_str)

    def if_exists(self, proj_id : int = None, abbrev_name : str = '', full_name : str = '', label : str = ''):
        if proj_id and abbrev_name:
            if int(proj_id) <= 0:
                raise Exception('INVALID Project ID! All Project IDs must be greater than 0')
            else:
                id_index = self.headers.index('project_id')
                name_index = self.headers.index('abbrev_name')
                for row in self.content:
                    if (row[id_index] == proj_id) and (row[name_index].lower() == abbrev_name.lower()):
                        return True
            return False
        elif proj_id:
            if int(proj_id) <= 0:
                raise Exception('INVALID Project ID! All Project IDs must be greater than 0')
            else:
                id_index = self.headers.index('project_id')
                for row in self.content:
                    if row[id_index] == proj_id:
                        return True
            return False
        elif abbrev_name:
            name_index = self.headers.index('abbrev_name')
            for row in self.content:
                if row[name_index].lower() == abbrev_name.lower():
                    return True
            return False
        elif full_name:
            name_index = self.headers.index('full_name')
            for row in self.content:
                if row[name_index].lower() == full_name.lower():
                    return True
            return False
        elif label:
            label_index = self.headers.index('first_label')
            for row in self.content:
                if row[label_index].lower() == label.lower():
                    return True
            return False
        else:
            raise Exception('EMPTY METHOD CALL! Method \'if_exists\' in '+self.__class__.__name__+' requires at least one parameter')
    
    def add_character(self, proj_id : int, abbrev_name : str, full_name : str, label):
        self.content.insert(0, [proj_id,abbrev_name,full_name,label])
        self.write_characters()
    
    def delete_project(self, proj_id : int):
        if not self.if_exists(proj_id=proj_id):
            raise Exception('NONEXISTANT Project ID! There is no row with Project ID = '+str(proj_id)+' in characters.csv')
        id_index = self.headers.index('project_id')
        i = 0
        while True:
            if self.content:
                was_pop = False
                for i in range(0,len(self.content)):
                    if self.content[i][id_index] == proj_id:
                        was_pop = True
                        self.content.pop(i)
                        break
                if was_pop:
                    continue
            break
        self.write_characters()

    def delete_character(self, abbrev_name : str, proj_id : int):
        if not self.if_exists(proj_id=proj_id, abbrev_name=abbrev_name):
            raise Exception('NONEXISTANT Character! There is no abbreviated character name \''+abbrev_name.lower()+'\' with Project ID = '+str(proj_id)+' in characters.csv')
        id_index = self.headers.index('project_id')
        name_index = self.headers.index('abbrev_name')
        i = 0
        while True:
            if self.content:
                was_pop = False
                for i in range(0,len(self.content)):
                    if (self.content[i][id_index] == proj_id) and (self.content[i][name_index] == abbrev_name):
                        was_pop = True
                        self.content.pop(i)
                        break
                if was_pop:
                    continue
            break
        self.write_characters()
    
    def delete_label (self, label : str):
        if not self.if_exists(label=label):
            raise Exception('NONEXISTANT Label! There is no row with First Label = '+str(label)+' in characters.csv')
        label_index = self.headers.index('first_label')
        i = 0
        while True:
            if self.content:
                was_pop = False
                for i in range(0,len(self.content)):
                    if self.content[i][label_index] == label:
                        was_pop = True
                        self.content.pop(i)
                        break
                if was_pop:
                    continue
            break
        self.write_characters()
    
    def delete_all_characters(self):
        self.content = []
        self.write_characters()