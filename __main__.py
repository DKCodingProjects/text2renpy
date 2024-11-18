from src.args import *
from src.proxy import *
from src.translate import *
from src.format.input.screenplay_input import *
from src.format.output.renpy_output import *
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
    text = r'{i} I am italicized{/i} i am not {i} iam though{/i}{i} me too!{/i}   {i}me three!{/i}'
    text = RenPy_Output._remove_duplicate_tags(text, 'i')
    text = RenPy_Output._maintain_spacing(text)
    print(text)
    # Tester.test_all()
    '''
    filepath = r'test\test_screenplays\test_script.txt'
    analyzer = analyzer_proxy.Analyzer_Proxy.get_instance(filepath)
    analyzer.analyze()
    reader = reader_proxy.Reader_Proxy.get_instance(filepath)
    reader.open()
    translator = screenplay_to_renpy.Screenplay_to_Renpy()
    while not reader.is_eof:
        curr_chunks, para_attribs = reader.readpart()
        translator.translate(text_chunks=curr_chunks, para_attribs=para_attribs)
    else:
        exit()
        '''


if __name__ == '__main__':
    main()