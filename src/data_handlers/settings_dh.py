from .data_handler import Data_Handler
import os

class Settings_DH(Data_Handler):
    def __init__(self):
        super().__init__(os.path.join('data', 'settings.csv'))
        self.limit = 1
        self.settings = dict()
        for header in self.headers:
            value = self.content[0][self.headers.index(header)]
            self.settings[header] = value
    
    def upgrade_settings(self):
        const_headers =  ['more_by_default']
        default_values = ['False'              ] # if a value requires user input, set value to None
        self._upgrade_content(const_headers, default_values)
    
    def write_settings(self):
        if len(self.content) <= self.limit:
            self._write(self.limit)
        else:
            raise Exception(f'FILE LIMIT REACHED! File limit of '+str(self.limit)+'\' rows in projects.csv reached! Delete a project to make room for more!\n\t(You can adjust the limit in src.data_handers.projects_dh if you want!)')
    
    def more_by_default(self):
        if self.settings['more_by_default'] == 'True':
            return True
        else:
            return False
    
    def set_more_by_default(self, value : bool):
        if value:
            self.settings['more_by_default'] = 'True'
        else:
            self.settings['more_by_default'] = 'False'