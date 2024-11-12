from src.args import *
from src.read import *
from src.proxy.reader_proxy import Reader_Proxy
from src.translate import *
from src.format.input.screenplay_input import *
from src.analyze.docx_analyzer import Docx_Analyzer
from test.tester import Tester
import xml.etree.ElementTree as et
###############################
import dev.sandbox as dev
import docx

def main():
    '''
    print('starting program...')
    argv = argv_parse.Argv_Parser()
    args = argv.parser.parse_args()
    arg_obj = args_obj.Args_Object()
    arg_obj.argparse_populate(args)
    arg_obj.print()
    '''
    # Tester.test_all()
    analyzer = Docx_Analyzer(r'test\test_screenplays\test_script.docx')
    analyzer.analyze()
    reader = Reader_Proxy.get_instance(r'test\test_screenplays\test_script.docx')
    reader.open()
    translator = screenplay_to_renpy.Screenplay_to_Renpy()
    while not reader.is_eof:
        curr_chunks, para_attribs = reader.readpart()
        translator.translate(text_chunks=curr_chunks, para_attribs=para_attribs)
    else:
        exit()


if __name__ == '__main__':
    main()