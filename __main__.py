from src.general.text_chunk import Text_Chunk
from src.read import *
from src.args import *
from src.translate import *
from src.general import *
from src.data.handlers import *
###############################
import dev.sandbox as dev
from test.tester import Tester
import sys

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
    hist_data.delete_history(1)
    hist_data.delete_all_history()
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