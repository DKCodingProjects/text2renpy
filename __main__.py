from src.args import *
from src.proxy import *
from src.translate import *
from src.format.input.screenplay_input import *
from src.format.output.renpy_output import *
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
    chunk1 = Text_Chunk('first chunk! ')
    chunk1.set_bold(True)
    chunk1.set_strike(True)
    chunk1.set_color('fff')
    chunk2 = Text_Chunk('second chunk!     ')
    chunk2.set_bold(True)
    chunk2.set_italic(True)
    chunk2.set_underline(True)
    chunk2.set_size(2.0)
    chunk3 = Text_Chunk('final chunk!')
    chunk3.set_italic(True)
    chunk3.set_strike(True)
    chunk3.set_size(-2.0)
    chunk3.set_color('eee')
    chunks = [chunk1, chunk2, chunk3]
    renpy_out = RenPy_Output.format_say(chunks)
    print(renpy_out)
    '''
    filepath = r'test\test_screenplays\test_script.docx'
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