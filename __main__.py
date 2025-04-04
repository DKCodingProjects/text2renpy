from src.general.text_chunk import Text_Chunk
from src.read import *
from src.args import *
from src.translate import *
from src.general import *
from src.data_handlers import *
###############################
import dev.sandbox as dev
from test.tester import Tester
import csv
import sys
import os

def _consolidate_chunks(text_chunks: list[Text_Chunk]) -> str:
        consolid_text: str = ''
        for chunk in text_chunks:
            consolid_text = consolid_text + chunk.get_text()
        return consolid_text

def main():
    print('Hello World!')
    '''
    print('starting program...')
    argv = argv_parse.Argv_Parser()
    args = argv.parser.parse_args()
    arg_obj = args_obj.Args_Object()
    arg_obj.argparse_populate(args)
    arg_obj.print()
    '''
    '''
    proj_data = proj_data_handler.Project_Data_Handler()
    proj_data.create_proj('some_project','C:\\Users\\Dependent User\\OneDrive\\Documents\\Ren\'Py Projects\\Ren\'Py Games\\check\\game')
    proj_data.create_proj('another_project','C:\\Users\\Dependent User\\OneDrive\\Documents\\Ren\'Py Projects\\Ren\'Py Games\\check\\game')
    proj_data.delete_proj('some_project')
    proj_data.create_proj('a_third_project','C:\\Users\\Dependent User\\OneDrive\\Documents\\Ren\'Py Projects\\Ren\'Py Games\\check\\game')
    # proj_data.delete_proj('another_project')
    proj_data.rename_proj('another_project', 'new_name')
    proj_data.delete_proj('a_third_project')
    try:
        proj_data.delete_proj('another_project')
    except Exception as err:
        print(err)
    proj_data.delete_proj('new_name')
    hist_data = hist_data_handler.History_Data_Handler()
    hist_data.add_history(1, 'writefile', 'readfile')
    hist_data.add_history(1, 'writefile', 'readfile')
    hist_data.add_history(2, 'writefile', 'readfile')
    hist_data.delete_project(1)
    hist_data.delete_history()'
    
    hist_data = data_handler.Data_Handler(os.path.join('data', 'history.csv'))
    char_data = data_handler.Data_Handler(os.path.join('data', 'characters.csv'))
    '''

    with open('data\\projects.csv', 'w', newline='') as bad_project:
        writer = csv.writer(bad_project)
        writer.writerow(['project_id','name','path','description','bad_header'])
        writer.writerow(['1','name2','path2','description','bad_value'])
        writer.writerow(['2','name3','path2','description2','bad_value2'])
    
    proj_data = data_handler.Data_Handler(os.path.join('data', 'projects.csv'))
    print(proj_data.content)
    proj_data._upgrade_content(['project_id','name','path','description'],[ None       , None , None , ''          ])
    print(proj_data.content)

    with open('data\\projects.csv', 'w', newline='') as bad_project:
        writer = csv.writer(bad_project)
        writer.writerow(['project_id','name','path'])
        writer.writerow(['1','name3','path2'])
        writer.writerow(['2','name3','path2'])
    
    proj_data = data_handler.Data_Handler(os.path.join('data', 'projects.csv'))
    print(proj_data.content)
    proj_data._upgrade_content(['project_id','name','path','description'],[ None       , None , None , ''          ])
    print(proj_data.content)

    with open('data\\projects.csv', 'w', newline='') as bad_project:
        writer = csv.writer(bad_project)
        writer.writerow(['name','path','project_id','description'])
        writer.writerow(['name3','path2','1','description'])
        writer.writerow(['name3','path2','2','desc'])
    
    proj_data = data_handler.Data_Handler(os.path.join('data', 'projects.csv'))
    print(proj_data.content)
    proj_data._upgrade_content(['project_id','name','path','description'],[ None       , None , None , ''          ])
    print(proj_data.content)

    with open('data\\projects.csv', 'w', newline='') as bad_project:
        writer = csv.writer(bad_project)
        writer.writerow(['name','path','project_id'])
        writer.writerow(['name3','path2','1'])
        writer.writerow(['name3','path2','2'])
    
    proj_data = data_handler.Data_Handler(os.path.join('data', 'projects.csv'))
    print(proj_data.content)
    proj_data._upgrade_content(['project_id','name','path','description'],[ None       , None , None , ''          ])
    print(proj_data.content)

    proj_data = data_handler.Data_Handler(os.path.join('data', 'projects.csv'))
    proj_data._remove_all()
    proj_data._write()
    
    '''
    proj_data._add_row(['1','name','path','description','img_format','chrctr_filename'])
    proj_data._add_row(['1','name1','path','description','img_format','chrctr_filename'])
    proj_data._add_row(['2','name2','path','description','img_format','chrctr_filename'])
    proj_data._add_row(['2','name3 3','path','description','img_format','chrctr_filename'])
    proj_data._update_row('project_id', '1', '3')
    print(proj_data.content)
    proj_data._remove_rows('project_id', '1')
    print(proj_data.content)
    proj_data._delete_row('project_id', '2')
    print(proj_data.content)
    proj_data._remove_all()
    proj_data._write()
    '''
    '''
    proj_data = proj_data_handler.Project_Data_Handler()
    proj_data.create_proj('some_project','C:\\Users\\Dependent User\\OneDrive\\Documents\\Ren\'Py Projects\\Ren\'Py Games\\check\\game')
    hist_data = hist_data_handler.History_Data_Handler()
    hist_data.add_history(1, 'writefile', 'readfile')
    char_data = char_data_handler.Character_Data_Handler()
    char_data.add_character(1,'nm','Name','label')
    proj_data.delete_proj('some_project')'
    '''
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