import argparse
import sys

'''
******************************************************************
The Help_Formatter class changes the format of the 
ArgumentParser's help menu (accessed via -h) to NOT show the 
metavar instead of showing it after every flag. Useful for visual 
clarity, and maintains metavar for access.
'''
class Help_Formatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        default = self._get_default_metavar_for_optional(action)
        return ', '.join(action.option_strings)

'''
******************************************************************
The Argv_Parser class stores all of the flags used on the command 
line by using an ArgumentParser. Also adds flag information which 
can be accessed when entering the -h or --help flag on the command
line.
'''
class Argv_Parser:
    def __init__(self):
        # lambda for formatting help menu in argparser
        fmt = lambda prog: Help_Formatter(prog)
        self.parser = argparse.ArgumentParser(usage=sys.argv[0] + ' -r [file options] -t [prog params] [prog options]', description='A collection of flags used by ' + sys.argv[0] + ' for the command line interface.', formatter_class=fmt)
        self.parser._optionals.title = 'arguments' # risky line of code, can break ArgumentParser in a future update
        
        # flags for file arguments, stored as string values
        # BASIC FLAGS
        self.parser.add_argument('-p', '--project', dest='PROJ', help='Set Ren\'Py project program will pull from')
        self.parser.add_argument('-r', '--readfile', dest='READ', help='Set file program will read from')
        self.parser.add_argument('-w', '--writefile', dest='WRITE', help='Set file program will write to AND set script label (must be unique!)')
        self.parser.add_argument('--delete-all', help='Delete all data (besides headers) stored in src/data. Yes, that means ALL data!')
        self.parser.add_argument('--cp', '--delete-project', dest='DELPROJ', help='Find Ren\'Py project via name. If found, delete all project data stored in projects, history, and characters.')
        
        # PROJECT FLAGS
        self.parser.add_argument('--cp', '--create-project', dest='NEWPROJ', help='Set Ren\'Py project name and create new project')
        self.parser.add_argument('--rp', '--rename-project', dest='NEWNAME', help='Rename Ren\'Py project that already exists')
        self.parser.add_argument('--ap', '--all-projects', help='Returns all project names currently stored')
        self.parser.add_argument('--fp', '--find-project', dest='FINDPROJ', help='Search for a Ren\'Py project by name. If found, set as project to manipulate.')
        self.parser.add_argument('--pd', '--project-directory', dest='PROJDIR', help='Set the Ren\'Py project game directory program will operate in')
        
        # HISTORY FLAGS
        self.parser.add_argument('--repeat', '--repeat-run', help='Repeat the latest run of text2renpy stored in the history')
        self.parser.add_argument('--dh', '--delete-history', help='Delete all data (besides headers) in project history')
        
        # CHARACTER FLAGS
        self.parser.add_argument('--ac', '--add-character', help='Repeat the latest run of text2renpy stored in the history')
        