import argparse
import sys

'''
******************************************************************
The Help_Formatter class changes the format of the 
ArgumentParser's help menu (accessed via -h) to NOT show the 
metavar instead of showing it after every flag. Useful for visual 
clarity, and maintains metavar.
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
        self.parser = argparse.ArgumentParser(description='A collection of flags used by ' + sys.argv[0] + ' for the command line interface.', formatter_class=fmt)
        self.parser._optionals.title = 'arguments' # risky line of code, can break ArgumentParser in a future update
        self.subparsers = self.parser.add_subparsers()
        
        # flags for file arguments, stored as string values
        # RUN FLAGS
        self.run_parser = self.subparsers.add_parser('run', help='Run the text2renpy program', formatter_class=fmt)
        self.run_parser.add_argument('-p', '--project', dest='PROJECT', metavar=('project_name'), help='enter the name of the text2renpy project to use during run', required=True)
        self.run_parser.add_argument('-r', '--read', dest='READ', metavar=('read_file'), help='enter a realtive/full path to reading file text2renpy will use to generate the Ren\'Py script', required=True)
        self.run_parser.add_argument('-w', '--write', dest='WRITE', metavar=('write_file'), help='enter the writing file\'s name that text2renpy will write output to; no path is required, just provide a valid filename', required=True)
        self.run_parser.add_argument('-l', '--label', dest='LABEL', metavar=('renpy_label'), help='set Ren\'Py script\'s code label. Optional, but (if not provided) the program uses the writefile\'s name as the label by default!')
        
        # PROJECT FLAGS
        self.projects_parser = self.subparsers.add_parser('project', help='access/configure text2renpy\'s project settings data', formatter_class=fmt)
        self.projects_parser.add_argument('--create', dest='SETPROJ', nargs=2, metavar=('project_name', 'project_directory'), help='create a text2renpy project; provide a unique project name and supply the full/realtive path to a Ren\'Py project\'s \'game\' directory')
        self.projects_parser.add_argument('--delete', dest='DELPROJ', metavar=('project_name'), help='delete a text2renpy project via name; this action deletes all data relating to the project')
        self.projects_parser.add_argument('--delete-all', dest='DELALLPROJ', action='store_true', help='delete all data stored in text2renpy; remeber, this action deletes ALL data')
        self.projects_parser.add_argument('--get', dest='GETPROJ', metavar=('project_name'), help='search for a text2renpy project by name')
        self.projects_parser.add_argument('--get-all', action='store_true', help='returns all project names currently stored')
        self.projects_parser.add_argument('--rename', dest='SETNAME', nargs=2, metavar=('project_name', 'new_name'), help='rename a text2renpy project that already exists')
        self.projects_parser.add_argument('--set-directory', dest='SETDIR', nargs=2, metavar=('project_name', 'new_directory'),help='set a text2renpy project\'s \'game\' directory')
        
        # HISTORY FLAGS
        self.history_parser = self.subparsers.add_parser('history', help='access text2renpy\'s run history data', formatter_class=fmt)
        self.history_parser.add_argument('--show', dest='SHOW', action='store_true', help='show all data stored in text2renpy\'s run history')
        self.history_parser.add_argument('--repeat', dest='REPEAT', action='store_true', help='repeat the latest run of text2renpy stored in the history')
        self.history_parser.add_argument('--clear', dest='CLEARHIST', action='store_true', help='delete all data stored in text2renpy\'s history data')
        
        # CHARACTER FLAGS
        self.characters_parser = self.subparsers.add_parser('character', help='configure a text2renpy project\'s Ren\'Py character data', formatter_class=fmt)
        self.characters_parser.add_argument('--add', dest='ADDCHRCTR', nargs=2, metavar=('project_name', 'character_name'), help='add a new character to text2renpy\'s characters data')
        self.characters_parser.add_argument('--delete', dest='DELCHRCTR', nargs=2, metavar=('project_name', 'character_name'), help='delete a character in text2renpy\'s characters data')
        self.characters_parser.add_argument('--delete-all', dest='DELALLCHRCTR', action='store_true', help='delete all data stored in text2renpy\'s characters data')
        