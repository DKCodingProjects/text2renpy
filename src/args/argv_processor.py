from src.general.text_chunk import Text_Chunk
from src.read import *
from src.args.argv_parse import Argv_Parser
from src.args.argv_namespaces import Settings_Namespace, Run_Namespace, Project_Namespace
from src.translate import *
from src.general import *
from src.data_handlers import *
import src.program_run

class Argv_Processor():
    def __init__(self):
        pass

    def all_attrbs(args, attrbs : list):
        if attrbs:
            all_found = True
            for attrb in attrbs:
                if not hasattr(args, attrb):
                    all_found = False
                    break
            return all_found
        else:
            return False

    def has_attrb(args, attrbs : list):
        for attrb in attrbs:
            if hasattr(args, attrb):
                return True
        return False
    
    def _remove_mangling(static_class : object):
        keys = list(vars(static_class).keys())
        pop_index = []
        pop_offset = 0
        for i in range(0,len(keys)):
            key = keys[i]
            if '__' in key:
                pop_index.append(i)
        for pop in pop_index:
            keys.pop(pop - pop_offset)
            pop_offset += 1
        return keys

    def is_settings(args):
        print()
        return Argv_Processor.has_attrb(args, Argv_Processor._remove_mangling(Settings_Namespace))
    
    def is_run(args):
        required_attrbs = ['PROJECT', 'READ']
        return Argv_Processor.all_attrbs(args, required_attrbs)
    
    def is_project(args):
        return Argv_Processor.has_attrb(args, Argv_Processor._remove_mangling(Project_Namespace))

    def is_history(args):
        project_attrbs = []
        return Argv_Processor.has_attrb(args, project_attrbs)

    def is_character(args):
        character_attrbs = []
        return Argv_Processor.has_attrb(args, character_attrbs)
        
    def run_commandline() -> int:
        settings = settings_dh.Settings_DH()
        # settings.set_more_by_default(True)
        argv = Argv_Parser(settings)
        args = argv.parser.parse_args()
        if Argv_Processor.is_settings(args):
            sett_namespace = Settings_Namespace()
            args = argv.parser.parse_args(namespace=sett_namespace)
            sett_data = settings_dh.Settings_DH()
            def _handle_bool(value : str = 'f'):
                if value == 't':
                    return True
                elif value == 'f':
                    return False
                else:
                    raise Exception('INVALID BOOLEAN: boolean values must be provided as \'t\' (True) or \'f\' (False)')
            if args.SHOWSETTINGS:
                sett_data.set_show_settings(_handle_bool(args.SHOWSETTINGS))
                print(sett_data.settings['show_settings'])
            if args.MOREBYDEFAULT:
                sett_data.set_more_by_default(_handle_bool(args.MOREBYDEFAULT))
            sett_data.write_settings()

        elif Argv_Processor.is_run(args):
            run_namespace = Run_Namespace()
            args = argv.parser.parse_args(namespace=run_namespace)
            proj_data = projects_dh.Projects_DH()
            project = program_run.Program_Run(args)
            print(project)

        elif Argv_Processor.is_project(args):
            proj_namespace = Project_Namespace()
            args = argv.parser.parse_args(namespace=proj_namespace)
            proj_data = projects_dh.Projects_DH()
            if args.SETPROJ:
                proj_data.create_proj(proj_name=args.SETPROJ[0], proj_path=args.SETPROJ[1])
            if args.SETNAME:
                proj_data.rename_proj(proj_name=args.SETNAME[0], new_name=args.SETNAME[1])
            if args.SETDIR:
                proj_data.update_path(proj_name=args.SETDIR[0], new_path=args.SETDIR[1])
            if args.SETDESC:
                desc_limit = 100
                if len(args.SETDESC) > desc_limit:
                    while True:
                        answer = input(f'WARNING: description for project \''+args.SETDESC[0]+'\' exceeds '+str(desc_limit)+' character limit!\nCan the program cut down the description to the maximum 100 character? (y/n): ')
                        if answer.lower() == 'y':
                            print('CONFIRMED: cutting down description to meet '+str(desc_limit)+' character limit...')
                            break
                        elif answer.lower() == 'n':
                            print(f'DENIED: program will not cut down description\nShutting down program...')
                            return 2
                        else:
                            print(f'INVALID ANSWER: type \'y\' (Yes) or \'n\' (No) as your answer.\nTry again...')
                proj_data.set_desc(proj_name=args.SETDESC[0], desc=(args.SETDESC[1] if len(args.SETDESC[1]) <= desc_limit else args.SETDESC[1][:desc_limit]))
            if args.DELPROJ:
                proj_data.delete_proj(proj_name=args.DELPROJ)
            if args.DELALL:
                proj_data.remove_all()
            if args.GETPROJ:
                project = proj_data.find_proj(proj_name=args.GETPROJ)
                print(project)
            if args.GETALL:
                all_projects = proj_data.content
                print(all_projects)
            proj_data.write_projects()

        elif Argv_Processor.is_history(args):
            pass
            # proj_data = projects_dh.Projects_DH()
            # project_id = None
            # project = proj_data.find_project(args.PROJECT)
            # if project:
            #     project_id = project[proj_data.headers.index('project_id')]
            # if project_id:
            #     hist_data = history_dh.History_DH()
            #     # handle history data changes

        elif Argv_Processor.is_character(args):
            pass
            # proj_data = projects_dh.Projects_DH()
            # project_id = None
            # project = proj_data.find_project(args.PROJECT)
            # if project:
            #     project_id = project[proj_data.headers.index('project_id')]
            # if project_id:
            #     char_data = characters_dh.Characters_DH()
            #     # handle character data changes

        else:
            return 1

        return 0