from src.args import *
from src.proxy import *
from src.translate import *
###############################
import dev.sandbox as dev
from test.tester import Tester
import sys

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
    '''
    Tester.test_all()
    filepath = r'test\test_screenplays\test_script.docx'
    reader = reader_proxy.Reader_Proxy.get_instance(filepath)
    reader.open()
    # Create translator proxy
    translator = screenplay_to_renpy.Screenplay_to_Renpy()
    while not reader.is_eof:
        curr_chunks, para_attribs = reader.readpart()
        scrnplay_type, renpy_statement = translator.translate(text_chunks=curr_chunks, para_attribs=para_attribs)
        if type != SCREENPLAY_TEXT.EMPTY:
            # print(f'{statement} : {type}')
            pass
    else:
        exit()
    '''
    '''
    def button_clicked():
        print("You clicked the button, didn't you!")

    app = QApplication()
    button = QPushButton("Press Me")

    #clicked is a signal of QPushButton. It's emitted when you click
    #  on the button
    #You can wire a slot to the signal using the syntax below : 
    button.clicked.connect(button_clicked)

    button.show()
    app.exec()
    '''


if __name__ == '__main__':
    main()