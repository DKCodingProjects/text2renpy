from .data_handler import Data_Handler
import os

class Settings_DH(Data_Handler):
    def __init__(self):
        super().__init__(os.path.join('data', 'settings.csv'))
        self.limit = 1
        self.settings = dict()
        for row in self.content:
            name = row[self.headers.index('setting_name')]
            value = row[self.headers.index('value')]
            self.settings[name] = value
    
    def upgrade_settings(self):
        # Needs new way of generating files since every row is a unique setting
        const_headers =  ['setting_name','value','description']
        default_values = ['False'              ] # if a value requires user input, set value to None
        # self._upgrade_content(const_headers, default_values)
    
    def write_settings(self):
        if len(self.content) <= self.limit:
            self._write(self.limit)
        else:
            raise Exception(f'FILE LIMIT REACHED! File limit of '+str(self.limit)+'\' rows in projects.csv reached! Delete a project to make room for more!\n\t(You can adjust the limit in src.data_handers.projects_dh if you want!)')
    
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
        return self._set_bool('show_settings')
    
    def more_by_default(self):
        return self._get_bool('more_by_default')
    
    def set_more_by_default(self, value : bool):
        return self._set_bool('more_by_default', value)