from .data_handler import Data_Handler
from datetime import datetime
import os

class History_DH(Data_Handler):
    def __init__(self):
        super().__init__(os.path.join('data', 'history.csv'))
        self.id_index = self.headers.index('project_id')
        self.limit = 100
    
    def upgrade_content(self):
        const_headers =  ['project_id','run_date','write_file','read_file']
        default_values = [ None       , None     , None       , None      ] # if a value requires user input, set value to None
        self._upgrade_content(const_headers, default_values)
    
    def write_history(self):
        self._write(self.limit)
        if len(self.content) > self.limit:
            raise Warning(f'FILE LIMIT REACHED! File limit of '+str(self.limit)+'\' rows in history.csv reached! Deleting oldest row in history.csv...')
            
    def _format_date():
        date = datetime.now()
        return date.strftime('%Y-%m-%d %H:%M:%S')
    
    def _default_hist(proj_id : str, write_file : str, read_file : str) -> list:
        return [proj_id,History_DH._format_date(),write_file,read_file]
    
    def get_recent(self):
        if self.content:
            return self.content[0]
        else:
            raise Exception('EMPTY CONTENT! File \'history.csv\' has no data in it to search!')
    
    def add_history(self, proj_id : str, write_file : str, read_file : str):
        self._add_row(History_DH._default_hist(proj_id, write_file, read_file),0)
    
    def delete_history(self, proj_id : str):
        if self._get_row('project_id',str(proj_id)):
            self._remove_rows('project_id',str(proj_id))
        else: 
            raise Exception('MISSING HISTORY! Program attempted to delete all rows with project_id \''+str(proj_id)+'\' but found nothing to delete!')
    
    def remove_all(self):
        self._remove_all()