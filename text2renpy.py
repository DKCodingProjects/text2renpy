from src.args import *
###############################
import dev.sandbox as dev
from test.tester import Tester
from argparse import HelpFormatter, RawTextHelpFormatter, RawDescriptionHelpFormatter
from src.data_handlers import *
import inspect
import csv
import os

def main():
    # print('starting program...')
    # members = vars(HelpFormatter)
    # print(members)
    # print(members['_fill_text'])
    # members = vars(RawTextHelpFormatter)
    # print(members)
    # members = vars(RawDescriptionHelpFormatter)
    # print(members)
    argv_processor.Argv_Processor.run_commandline()
    # print(settings_dh.Default_Settings.default_names)
    # sett_data = settings_dh.Settings_DH()
    # sett_data.content = [['show_settings', 'boolean', 'False', "If True, the program's settings will be displayed in text2renpy's core help menu (python text2renpy.py -h)"], ['more_by_default', 'boolean', 'False', "A toggle which determines if more subcommand (run, project, etc) arguments are available without the 'more' subcommand prefix (True), or are only available with the 'more' subcommand prefix (False)"],['bad_setting',  'boolean','False',"If True, the program's settings will be displayed in text2renpy's core help menu (python text2renpy.py -h)"]]
    # sett_data.upgrade_settings()
    # print(sett_data.content)
    # with open('data\\projects.csv', 'w', newline='') as bad_project:
    #     writer = csv.writer(bad_project)
    #     writer.writerow(['project_id','name','path','description','bad_header'])
    #     writer.writerow(['1','name2','path2','description','bad_value'])
    #     writer.writerow(['2','name3','path2','description2','bad_value2'])
    
    # proj_data = data_handler.Data_Handler(os.path.join('data', 'projects.csv'))
    # print(proj_data.content)
    # proj_data._upgrade_content(['project_id','name','path','description'],[ None       , None , None , ''          ])
    # print(proj_data.content)

    # with open('data\\projects.csv', 'w', newline='') as bad_project:
    #     writer = csv.writer(bad_project)
    #     writer.writerow(['project_id','name','path'])
    #     writer.writerow(['1','name3','path2'])
    #     writer.writerow(['2','name3','path2'])
    
    # proj_data = data_handler.Data_Handler(os.path.join('data', 'projects.csv'))
    # print(proj_data.content)
    # proj_data._upgrade_content(['project_id','name','path','description'],[ None       , None , None , ''          ])
    # print(proj_data.content)

    # with open('data\\projects.csv', 'w', newline='') as bad_project:
    #     writer = csv.writer(bad_project)
    #     writer.writerow(['name','path','project_id','description'])
    #     writer.writerow(['name3','path2','1','description'])
    #     writer.writerow(['name3','path2','2','desc'])
    
    # proj_data = data_handler.Data_Handler(os.path.join('data', 'projects.csv'))
    # print(proj_data.content)
    # proj_data._upgrade_content(['project_id','name','path','description'],[ None       , None , None , ''          ])
    # print(proj_data.content)

    # with open('data\\projects.csv', 'w', newline='') as bad_project:
    #     writer = csv.writer(bad_project)
    #     writer.writerow(['name','path','project_id'])
    #     writer.writerow(['name3','path2','1'])
    #     writer.writerow(['name3','path2','2'])
    
    # proj_data = data_handler.Data_Handler(os.path.join('data', 'projects.csv'))
    # print(proj_data.content)
    # proj_data._upgrade_content(['project_id','name','path','description'],[ None       , None , None , ''          ])
    # print(proj_data.content)

    # proj_data = data_handler.Data_Handler(os.path.join('data', 'projects.csv'))
    # proj_data._remove_all()
    
    
    # proj_data._add_row(['1','name','path','description','img_format','chrctr_filename'])
    # proj_data._add_row(['1','name1','path','description','img_format','chrctr_filename'])
    # proj_data._add_row(['2','name2','path','description','img_format','chrctr_filename'])
    # proj_data._add_row(['2','name3 3','path','description','img_format','chrctr_filename'])
    # proj_data._update_row('project_id', '1', '3')
    # print(proj_data.content)
    # proj_data._remove_rows('project_id', '1')
    # print(proj_data.content)
    # proj_data._delete_row('project_id', '2')
    # print(proj_data.content)
    # proj_data._remove_all()
    
    
    # proj_data = projects_dh.Projects_DH()
    # proj_data.create_proj('some_project','C:\\Users\\Dependent User\\OneDrive\\Documents\\Ren\'Py Projects\\Ren\'Py Games\\check\\game')
    # proj_data.create_proj('some_project2','C:\\Users\\Dependent User\\OneDrive\\Documents\\Ren\'Py Projects\\Ren\'Py Games\\check\\game')
    # print(proj_data.content)
    # print(proj_data._search({'project_id' : '1', 'name' : 'some_project'}))
    # print(proj_data.content)
    # proj_data.rename_proj('some_project', 'better_project')
    # hist_data = history_dh.History_DH()
    # hist_data.add_history('1', 'writefile', 'readfile')
    # hist_data.add_history('2', 'writefile', 'readfile')
    # hist_data.add_history('1', 'writefile2', 'readfile')
    # hist_data.add_history('1', 'writefile', 'readfile')
    # print(hist_data.content)
    # print(hist_data._search({'project_id' : '1', 'write_file' : 'writefile'}, -1))
    # # char_data = char_data_handler.Character_Data_Handler()
    # # char_data.add_character(1,'nm','Name','label')
    # proj_data.delete_proj('better_project')
    # print(proj_data.content)
    # hist_data.delete_history('1')
    # print(hist_data.content)
    # char_data = characters_dh.Characters_DH()
    # char_data.add_character('1', 'bi', 'BigDick', 'label')
    # char_data.add_character('1', 'bi', 'BigDick', 'label')
    # char_data.add_character('2', 'bi3', 'BigDick3', 'label')
    # char_data.add_character('1', 'bi', 'BigDick', 'label')
    # print(char_data.content)
    # char_data.delete_character('1', 'bi')
    # print(char_data.content)
    # char_data.delete_project('1')
    # print(char_data.content)
    
    # GUI/ Command-line interface
    # Pass project info to program
    # Tester.test_all()
    # filepath = r'test\\test_documents\\test_script.docx'
    # reader = reader_proxy.Reader_Proxy.get_instance(filepath)
    # reader.open()
    # # Create translator proxy
    # while not reader.is_eof:
    #     curr_text = _consolidate_chunks(reader.readpart())
    #     if curr_text:
    #         print(curr_text)
    # else:
    #     exit()

if __name__ == '__main__':
    main()