import argparse
import sys

class Help_Formatter(argparse.HelpFormatter):
    def _fill_text(self, text, width, indent):
        raw = argparse.RawDescriptionHelpFormatter(self._prog)
        return raw._fill_text(text, width, indent)
    
    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        default = self._get_default_metavar_for_optional(action)
        return ', '.join(action.option_strings)

class Argv_Parser:
    def __init__(self, settings : object): # object is text2renpy.Settings
        # lambda for formatting help menu in argparser
        fmt = lambda prog: Help_Formatter(prog)
        prog_name = sys.argv[0].removesuffix('.py')
        self.parser = argparse.ArgumentParser(description=f'a collection of flags used by ' + prog_name + f' for the command line interface.\n\ncurrent program settings:\n  - more options by default = ' + str(settings.more_by_default()), formatter_class=fmt)
        self.parser.add_argument('--more-by-default', dest='MOREBYDEFAULT', metavar=('(t,f)'), help='if true (t), all ' + prog_name + ' subcommands (run, project, history, etc) will access MORE options by default. if false (f), only \'more\' subcommands will  contain all flags and args (default behavior)')
        self.subparsers = self.parser.add_subparsers()
        
        # flags for file arguments, stored as string values
        # RUN FLAGS
        p_flag, project_flag, proj_dest, project_metavars, project_help, project_required = '-p', '--project', 'PROJECT', ('project_name'), 'enter the name of the ' + prog_name + ' project to use during run', True
        r_flag, read_flag, read_dest, read_metavars, read_help, read_required = '-r', '--read', 'READ', ('read_file'), 'enter a realtive/full path to reading file ' + prog_name + ' will use to generate the Ren\'Py script', True
        w_flag, write_flag, write_dest, write_metavars, write_help = '-w', '--write', 'WRITE', ('write_file'), 'enter the writing file\'s name that ' + prog_name + ' will write output to (if not provided, uses readfile\'s name by default)'
        m_flag, mode_flag, mode_default, mode_dest, mode_metavars, mode_help = '-m', '--write-mode', 'w', 'WRITEMODE', ('(w,o,a)'), 'enter the write mode: \'w\' is a normal write that warns of overwriting (default), \'o\' overwrites a file if it already exists, and \'a\' appends to a file'
        t_flag, test_flag, test_dest, test_action, test_help = '-t', '--test', 'TEST', 'store_true', 'run ' + prog_name + ' without generating final Ren\'Py script. Useful for debugging; check logs to see program output'
        # MORE RUN FLAGS
        label_flag, label_dest, label_metavars, label_help = '--label', 'LABEL', ('renpy_label'), 'set Ren\'Py script\'s code label. if not provided, the program uses the writefile\'s name by default (if no label is found within the readfile)!'
        log_flag, log_dest, log_metavars, log_help = '--set-log', 'LOG', ('log_file'), 'set where logging output will be written to; log files are written to ' + prog_name + '\'s log directory by default'
        report_flag, report_dest, report_metavars, report_help = '--set-report', 'REPORT', ('report_file'), 'set where report output will be written to; report files are written to a project\'s game directory by default'
        reset_flag, reset_dest, reset_action, reset_help = '--reset-report', 'RESETREPORT', 'store_true', 'reset a project\'s report file before writing'
        noreport_flag, noreport_dest, noreport_action, noreport_help = '--no-report', 'NOREPORT', 'store_true', 'prevent ' + prog_name + ' from updating or creating a project\'s report file'
        # _flag, _flag, _dest, _help = 

        # RUN ARGS
        self.run_parser = self.subparsers.add_parser('run', help='run the ' + prog_name + ' program'+(' with MORE options' if settings.more_by_default() else ''), formatter_class=fmt)
        self.run_parser.add_argument(p_flag, project_flag, dest=proj_dest, metavar=project_metavars, help=project_help, required=project_required)
        self.run_parser.add_argument(r_flag, read_flag, dest=read_dest, metavar=read_metavars, help=read_help, required=read_required)
        self.run_parser.add_argument(w_flag, write_flag, dest=write_dest, metavar=write_metavars, help=write_help)
        self.run_parser.add_argument(m_flag, mode_flag, default=mode_default, dest=mode_dest, metavar=mode_metavars, help=mode_help)
        self.run_parser.add_argument(t_flag, test_flag, dest=test_dest, action=test_action, help=test_help)
        if settings.more_by_default():
            self.run_parser.add_argument(label_flag, dest=label_dest, metavar=label_metavars, help=label_help)
            self.run_parser.add_argument(log_flag, dest=log_dest, metavar=log_metavars, help=log_help)
            self.run_parser.add_argument(report_flag, dest=report_dest, metavar=report_metavars, help=report_help)
            self.run_parser.add_argument(reset_flag, dest=reset_dest, action=reset_action, help=reset_help)
            self.run_parser.add_argument(noreport_flag, dest=noreport_dest, action=noreport_action, help=noreport_help)
        
        # PROJECT FLAGS
        create_flag, create_dest, create_nargs, create_metavars, create_help = '--create', 'SETPROJ', 2, ('project_name', 'renpy_game'), 'create a ' + prog_name + ' project; provide a unique project name and supply the full/realtive path to a Ren\'Py project\'s \'game\' directory'
        delete_flag, delete_dest, delete_metavars, delete_help = '--delete', 'DELPROJ', ('project_name'), 'delete a ' + prog_name + ' project via name; this action deletes all data relating to the project stored in other csv files too'
        deleteall_flag, deleteall_dest, deleteall_action, deleteall_help = '--delete-all', 'DELALL', 'store_true', 'CAUTION: this action deletes ALL ' + prog_name + ' data'
        get_flag, get_dest, get_metavars, get_help = '--get', 'GETPROJ', ('project_name'), 'search for a ' + prog_name + ' project by name'
        getall_flag, getall_dest, getall_action, getall_help = '--get-all', 'GETALL', 'store_true', 'returns all project names currently stored'
        rename_flag, rename_dest, rename_nargs, rename_metavars, rename_help = '--rename', 'SETNAME', 2, ('project_name', 'new_name'), 'rename a ' + prog_name + ' project that already exists'
        setdir_flag, setdir_dest, setdir_nargs, setdir_metavars, setdir_help = '--set-game-directory', 'SETDIR', 2, ('project_name', 'new_game'), 'set a ' + prog_name + ' project\'s path to a Ren\'py project\'s \'game\' directory'
        desc_flag, desc_dest, desc_nargs, desc_metavars, desc_help = '--set-description', 'SETDESC', 2, ('project_name', '"description"'), 'set a '+ prog_name + ' project\'s description (MAX 100 characters)'
        # MORE PROJECT FLAGS
        
        # PROJECT ARGS
        self.projects_parser = self.subparsers.add_parser('project', help='access/configure ' + prog_name + '\'s project settings data'+(' with MORE options' if settings.more_by_default() else ''), formatter_class=fmt)
        self.projects_parser.add_argument(create_flag, dest=create_dest, nargs=create_nargs, metavar=create_metavars, help=create_help)
        self.projects_parser.add_argument(delete_flag, dest=delete_dest, metavar=delete_metavars, help=delete_help)
        self.projects_parser.add_argument(deleteall_flag, dest=deleteall_dest, action=deleteall_action, help=deleteall_help)
        self.projects_parser.add_argument(get_flag, dest=get_dest, metavar=get_metavars, help=get_help)
        self.projects_parser.add_argument(getall_flag, dest=getall_dest, action=getall_action, help=getall_help)
        self.projects_parser.add_argument(rename_flag, dest=rename_dest, nargs=rename_nargs, metavar=rename_metavars, help=rename_help)
        self.projects_parser.add_argument(setdir_flag, dest=setdir_dest, nargs=setdir_nargs, metavar=setdir_metavars, help=setdir_help)
        if settings.more_by_default():
            self.projects_parser.add_argument(desc_flag, dest=desc_dest, nargs=desc_nargs, metavar=desc_metavars, help=desc_help)
        
        # # HISTORY FLAGS
        # self.history_parser = self.subparsers.add_parser('history', help='access ' + prog_name + '\'s run history data', formatter_class=fmt)
        # self.history_parser.add_argument('--show', dest='SHOW', action='store_true', help='show all data stored in ' + prog_name + '\'s run history')
        # self.history_parser.add_argument('--repeat', dest='REPEAT', action='store_true', help='repeat the latest run of ' + prog_name + ' stored in the history')
        # # self.history_parser.add_argument('--repeat-project', dest='REPEATPROJ', help='repeat the latest run of ' + prog_name + ' stored in the history')
        # self.history_parser.add_argument('--clear', dest='CLEAR', action='store_true', help='delete all data stored in ' + prog_name + '\'s history data')
        
        # # CHARACTER FLAGS
        # self.characters_parser = self.subparsers.add_parser('character', help='configure ' + prog_name + '\'s Ren\'Py character data', formatter_class=fmt)
        # self.characters_parser.add_argument('--add', dest='ADDCHRCTR', nargs=2, metavar=('project_name', 'character_name'), help='add a new character to ' + prog_name + '\'s characters data')
        # self.characters_parser.add_argument('--delete', dest='DELCHRCTR', nargs=2, metavar=('project_name', 'character_name'), help='delete a character in ' + prog_name + '\'s characters data')
        # self.characters_parser.add_argument('--delete-all', dest='DELALLCHRCTR', action='store_true', help='delete all data stored in ' + prog_name + '\'s characters data')

        self.more_parser = self.subparsers.add_parser('more', help=('(recommended for experienced users) access/configure more ' + prog_name + ' functionality' if not settings.more_by_default() else '*not available'), formatter_class=fmt)
        self.more_subparsers = self.more_parser.add_subparsers()
        if not settings.more_by_default():
            # MORE RUN ARGS
            self.more_run = self.more_subparsers.add_parser('run', help='run the ' + prog_name + ' program with more options', formatter_class=fmt)
            self.more_run.add_argument(p_flag, project_flag, dest=proj_dest, metavar=project_metavars, help=project_help, required=project_required)
            self.more_run.add_argument(r_flag, read_flag, dest=read_dest, metavar=read_metavars, help=read_help, required=read_required)
            self.more_run.add_argument(w_flag, write_flag, dest=write_dest, metavar=write_metavars, help=write_help)
            self.more_run.add_argument(m_flag, mode_flag, default=mode_default, dest=mode_dest, metavar=mode_metavars, help=mode_help)
            self.more_run.add_argument(t_flag, test_flag, dest=test_dest, action=test_action, help=test_help)
            self.more_run.add_argument(label_flag, dest=label_dest, metavar=label_metavars, help=label_help)
            self.more_run.add_argument(log_flag, dest=log_dest, metavar=log_metavars, help=log_help)
            self.more_run.add_argument(report_flag, dest=report_dest, metavar=report_metavars, help=report_help)
            self.more_run.add_argument(reset_flag, dest=reset_dest, action=reset_action, help=reset_help)
            self.more_run.add_argument(noreport_flag, dest=noreport_dest, action=noreport_action, help=noreport_help)

            # OTHER
            self.more_project = self.more_subparsers.add_parser('project', help='access/configure ' + prog_name + '\'s project settings data with more options', formatter_class=fmt)
            self.more_project.add_argument(create_flag, dest=create_dest, nargs=create_nargs, metavar=create_metavars, help=create_help)
            self.more_project.add_argument(delete_flag, dest=delete_dest, metavar=delete_metavars, help=delete_help)
            self.more_project.add_argument(deleteall_flag, dest=deleteall_dest, action=deleteall_action, help=deleteall_help)
            self.more_project.add_argument(get_flag, dest=get_dest, metavar=get_metavars, help=get_help)
            self.more_project.add_argument(getall_flag, dest=getall_dest, action=getall_action, help=getall_help)
            self.more_project.add_argument(rename_flag, dest=rename_dest, nargs=rename_nargs, metavar=rename_metavars, help=rename_help)
            self.more_project.add_argument(setdir_flag, dest=setdir_dest, nargs=setdir_nargs, metavar=setdir_metavars, help=setdir_help)
            self.more_project.add_argument(desc_flag, dest=desc_dest, nargs=desc_nargs, metavar=desc_metavars, help=desc_help)
        else:
            self.none_parser = self.more_subparsers.add_parser('None', help='there are no subcommands! use --more-by-default flag and set to \'f\' (false) to see them!', usage='a mystery...', description='you have discovered the realm of forbidden functionality. what will you do?', formatter_class=fmt)
            self.none_parser.add_argument('--throw-hand', dest='HAND', help='face an opponent, throw \'rock\', \'paper\', or \'scissors\'')
            self.none_parser.add_argument('--the-abyss', dest='BUTTON', action='store_true', help='what have you done...')
        
        