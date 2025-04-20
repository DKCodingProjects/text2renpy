from .data_handler import Data_Handler
import csv
import os

class Default_Settings():
    default_headers : tuple = ('setting_name','data_type','value','description')
    default_rows : tuple[tuple] = (
        ('show_settings',  'boolean','False',"If True, the program's settings will be displayed in text2renpy's core help menu (python text2renpy.py -h)"),
        ('more_by_default','boolean','False',"A toggle which determines if more subcommand (run, project, etc) arguments are available without the 'more' subcommand prefix (True), or are only available with the 'more' subcommand prefix (False)")
    )
    names = list()
    for row in default_rows:
        names.append(row[default_headers.index('setting_name')])
    default_names = set(names)
    del names

class Settings_DH(Data_Handler):
    def __init__(self):
        super().__init__(os.path.join('data', 'settings.csv'))
        self.settings = dict()
        for row in self.content:
            name = row[self.headers.index('setting_name')]
            value = row[self.headers.index('value')]
            self.settings[name] = value
    
    def upgrade_settings(self):
        const_headers = Default_Settings.default_headers
        self._upgrade_content(const_headers, [None for _ in range(len(const_headers))])
        skip_row = set()
        append_row = list()
        for default_row in Default_Settings.default_rows:
            found_setting = False
            for i in range(0,len(self.content)):
                if i in skip_row:
                    continue
                row = self.content[i]
                if default_row[const_headers.index('setting_name')] == row[const_headers.index('setting_name')]:
                    found_setting = True
                    skip_row.add(i)
                    for j in range(0,len(default_row)):
                        if not row[j]:
                            self.content[i][j] = default_row[j]
                elif row[const_headers.index('setting_name')] not in Default_Settings.default_names:
                    self.content.pop(i)
            if not found_setting:
                append_row.append(default_row)
        for row in append_row:
            self.content.append(list(row))
    
    def write_settings(self):
        with open(self.path, 'w', newline='') as write_project:
            csv_writer = csv.writer(write_project, quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(self.headers)
            for row in self.content:
                row[self.headers.index('value')] = self.settings[row[self.headers.index('setting_name')]]
                csv_writer.writerow(row)
    
    def _get_bool(self, column_name : str):
        if self.settings[column_name] == 'True':
            return True
        else:
            return False
    
    def _set_bool(self, column_name : str, value : bool):
        if value:
            self.settings[column_name] = 'True'
        else:
            self.settings[column_name] = 'False'

    def show_settings(self):
        return self._get_bool('show_settings')
    
    def set_show_settings(self, value : bool):
        return self._set_bool('show_settings', value)
    
    def more_by_default(self):
        return self._get_bool('more_by_default')
    
    def set_more_by_default(self, value : bool):
        return self._set_bool('more_by_default', value)