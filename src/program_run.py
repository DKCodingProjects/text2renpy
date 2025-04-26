from .args.argv_namespaces import Run_Namespace
from .data_handlers.projects_dh import Projects_DH
from datetime import datetime
from .data_handlers import *
import os

import logging
logger = logging.getLogger(__name__)

class Program_Run():
    FORMAT = '%(asctime)s> [%(levelname)s] %(message)s'

    def __init__(self, args : Run_Namespace, proj_data : Projects_DH = Projects_DH()):
        self.validate(args, proj_data)
    
    def validate(self, args : Run_Namespace, proj_data : Projects_DH):
        if args.LOG:
            logging.basicConfig(filename=args.LOG, level=logging.INFO, format=Program_Run.FORMAT, filemode="w")
            logger.info('Logging to '+args.LOG)
        else:
            logging.basicConfig(filename=os.path.join('logs', 'text2renpy.log'), level=logging.INFO, format=Program_Run.FORMAT, filemode="w")
            logger.info('Logging to '+os.path.join('logs', 'text2renpy.log')+' (default)')
        
        logger.info('')
        logger.info('Validating Run...')
        logger.info('Storing arguments...')
        self.run_args = args
        logger.info('SUCCESS: Arguments stored')

        logger.info('')
        logger.info('Gathering Project Data...')
        try:
            proj_data.headers
        except Exception as err:
            logger.error('FAILURE: an Exception occured ('+f"{type(err).__name__}: {err}"+')')
            return 1
        logger.info('SUCCESS: Accessed projects.csv data')
        if proj_data.content:
            logger.info('SUCCESS: projects.csv contains data!')
        else:
            logger.warning('FAILURE: no data found in projects.csv! Exiting run...')
            return 2
        
        logger.info('')
        logger.info('Looking for project \''+args.PROJECT+'\'...')
        try:
            row = proj_data.find_proj(self.run_args.PROJECT)[0]
        except Exception as err:
            logger.error('FAILURE: an Exception occured while finding project ('+f"{type(err).__name__}: {err}"+')')
            return 3
        if row:
            logger.info('SUCCESS: Project \''+args.PROJECT+'\' was found!')
        else:
            logger.error('FAILURE: The project does not exist! Exiting run...')
            return 4
        
        logger.info('')
        logger.info('Getting project id from project \''+args.PROJECT+'\'...')
        try:
            self.project_id = row[proj_data.headers.index('project_id')]
        except Exception as err:
            logger.error('FAILURE: an Exception occured while finding id ('+f"{type(err).__name__}: {err}"+')')
            return 5
        logger.info('SUCCESS: project \''+args.PROJECT+'\' has id of '+str(self.project_id))

        logger.info('')
        logger.info('Getting project path from project \''+args.PROJECT+'\'...')
        try:
            self.project_path = row[proj_data.headers.index('path')]
        except Exception as err:
            logger.error('FAILURE: an Exception occured while finding path ('+f"{type(err).__name__}: {err}"+')')
            return 6
        logger.info('SUCCESS: path to Ren\'Py project is '+self.project_path)

        self.read_file = self.run_args.READ

        logger.info('')
        logger.info('Testing access and format of readfile '+self.read_file)
        file, extension = os.path.splitext(self.read_file)
        if extension == '.docx':
            logger.info('SUCCESS: readfile is a docx file.')
        else:
            logger.error('FAILURE: readfile isn\'t a docx file! Exiting run...')
            return 7
        try:
            read_access = os.access(self.read_file, os.R_OK)
        except Exception as err:
            logger.error('FAILURE: an Exception occured while accessing readfile ('+f"{type(err).__name__}: {err}"+')')
            return 8
        if read_access:
            logger.info('SUCCESS: readfile exists with reading permissions.')
        else:
            logger.error('FAILURE: readfile doesn\'t exist or lacks reading permissions! Exiting run...')
            return 9
        
        logger.info('')
        logger.info('project and readfile vaildated. Ready for run!')

    def run(self):
        logger.info('')
        logger.info('Starting Run...')