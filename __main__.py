from src.general.text_chunk import Text_Chunk
from src.read import *
from src.args import *
from src.translate import *
from src.general import *
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
    # GUI/ Command-line interface
    # Pass project info to program
    # Tester.test_all()
    # filepath = r'test\test_documents\test_script.docx'
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