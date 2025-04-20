from args.argv_namespaces import Run_Namespace
from datetime import datetime
from data_handlers import *
import os

import logging
logger = logging.getLogger(__name__)

class Program_Run():
    
    def __init__(self, args : Run_Namespace):
        FORMAT = '%(asctime)s> %(message)s'
        if args.LOG:
            logging.basicConfig(filename=args.LOG, level=logging.INFO, format=FORMAT)
            logger.info('Logging to '+args.LOG)
        else:
            logging.basicConfig(filename=os.path.join('logs', 'text2renpy.log'), level=logging.INFO)
            logger.info('Logging to '+os.path.join('logs', 'text2renpy.log')+' (default)')
        
        logger.info('Starting Run...')
        self.run_args = args

        logger.info('Gathering Project Data...')
        proj_data = projects_dh.Projects_DH()
        logger.info('SUCCESS: Accessed projects.csv data')
        if proj_data.content:
            logger.info('- projects.csv contains data! Continuing run...')
        else:
            logger.info('- NO DATA found in projects.csv! Exiting run with status 1...')
            return 1
        logger.info('Looking for project \''+args.PROJECT+'\'...')
        row = proj_data.find_proj(self.run_args.PROJECT)
        if row:
            logger.info('SUCCESS: Project \''+args.PROJECT+'\' was found! Continuing run...')
        else:
            logger.info('FAILURE: The project does not exist! Exiting run with status 2...')
            return 2
        logger.info('Getting project id from project\''+args.PROJECT+'\'...')
        self.project_id = row[proj_data.headers.index('project_id')]
        logger.info('SUCCESS: project \''+args.PROJECT+'\' has id of '+str(self.project_id))
        logger.info('Getting project path from project\''+args.PROJECT+'\'...')
        self.project_path = row[proj_data.headers.index('path')]
        logger.info('SUCCESS: project path is '+self.project_path)

        


        self.read_file = self.run_args.READ


    def run(self):
        pass