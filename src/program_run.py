from .args.argv_namespaces import Run_Namespace
from .data_handlers.projects_dh import Projects_DH
from datetime import datetime
from .data_handlers import *
import os

import logging
logger = logging.getLogger(__name__)

class Program_Run():
    FORMAT = '%(asctime)s> %(message)s'

    def __init__(self, args : Run_Namespace):
        self.validate(args, projects_dh.Projects_DH())
    
    def validate(self, args : Run_Namespace, proj_data : Projects_DH):
        if args.LOG:
            logging.basicConfig(filename=args.LOG, level=logging.INFO, format=Program_Run.FORMAT)
            logger.info('Logging to '+args.LOG)
        else:
            logging.basicConfig(filename=os.path.join('logs', 'text2renpy.log'), level=logging.INFO, format=Program_Run.FORMAT)
            logger.info('Logging to '+os.path.join('logs', 'text2renpy.log')+' (default)')
        
        logger.info('\n')
        logger.info('Validating Run...')
        logger.info('Storing arguments...')
        self.run_args = args
        logger.info('SUCCESS: Arguments stored')

        logger.info('\n')
        logger.info('Gathering Project Data...')
        try:
            proj_data.headers
        except Exception as err:
            logger.error('Failed to gather project data, message : ('+err+')')
            return 1
        logger.info('SUCCESS: Accessed projects.csv data')
        if proj_data.content:
            logger.info('projects.csv contains data! Continuing run...')
        else:
            logger.info('NO DATA found in projects.csv! Exiting run...')
            return 2
        
        logger.info('\n')
        logger.info('Looking for project \''+args.PROJECT+'\'...')
        try:
            row = proj_data.find_proj(self.run_args.PROJECT)
        except Exception as err:
            logger.error('Failed to find project, message : ('+err+')')
            return 3
        if row:
            logger.info('SUCCESS: Project \''+args.PROJECT+'\' was found! Continuing run...')
        else:
            logger.info('FAILURE: The project does not exist! Exiting run...')
            return 4
        
        logger.info('\n')
        logger.info('Getting project id from project \''+args.PROJECT+'\'...')
        try:
            self.project_id = row[proj_data.headers.index('project_id')]
        except Exception as err:
            logger.error('Failed to gather project id, message : ('+err+')')
            return 5
        logger.info('SUCCESS: project \''+args.PROJECT+'\' has id of '+str(self.project_id))

        logger.info('\n')
        logger.info('Getting project path from project \''+args.PROJECT+'\'...')
        try:
            self.project_path = row[proj_data.headers.index('path')]
        except Exception as err:
            logger.error('Failed to gather project path, message : ('+err+')')
            return 6
        logger.info('SUCCESS: path to Ren\'Py project is '+self.project_path+'. Continuing run...')

        self.read_file = self.run_args.READ

        logger.info('\n')
        logger.info('Testing access and format of readfile \''+self.read_file+'\'...')
        file, extension = os.path.splitext(self.read_file)
        if extension == '.docx':
            logger.info('SUCCESS: readfile is a docx file. Continuing run...')
        else:
            logger.info('FAILURE: readfile isn\'t a docx file! Exiting run...')
            return 7
        try:
            read_access = os.access(self.read_file, os.R_OK)
        except Exception as err:
            logger.error('Failed to gather validate readfile, message : ('+err+')')
            return 8
        if read_access:
            logger.info('SUCCESS: readfile exists with reading permissions. Continuing run...')
        else:
            logger.info('FAILURE: readfile doesn\'t exist or lacks reading permissions! Exiting run...')
            return 9
        
        logger.info('\n')
        logger.info('project and readfile vaildated. Ready for run!')

    def run(self):
        logger.info('\n')
        logger.info('Starting Run...')