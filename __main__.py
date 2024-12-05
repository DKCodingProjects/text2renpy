from src.args import *
from src.proxy import *
from src.translate import *
from src.format.input.screenplay_input import *
from src.format.output.renpy_output import *
###############################
import dev.sandbox as dev
from test.tester import Tester
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

def main():
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
    number = 500000
    list_var: list = []
    set_var: set = {0}
    dict_var: dict = {}

    for i in range(0, number):
        list_var.append(str(i))
        dict_var[str(i)] = 0
    
    tuple_var: tuple = tuple(list_var)
    set_var = set(list_var)

    # access time
    second_num = 6000

    list_avg = 0.0
    set_avg = 0.0
    tuple_avg = 0.0
    dict_avg = 0.0

    for i in range(0, second_num):
        rand_int = str(randint(0, number-1))
        list_start = time()
        if rand_int in list_var:
            list_end = time() - list_start
            list_avg += list_end
        set_start = time()
        if rand_int in set_var:
            set_end = time() - set_start
            set_avg += set_end
        tuple_start = time()
        if rand_int in tuple_var:
            tuple_end = time() - tuple_start
            tuple_avg += tuple_end
        dict_start = time()
        if rand_int in dict_var.keys():
            dict_end = time() - dict_start
            dict_avg += dict_end

    print('list access average time = ', list_avg/second_num)
    print('set access average time = ', set_avg/second_num)
    print('tuple access average time = ', tuple_avg/second_num)
    print('dict access average time = ', dict_avg/second_num)
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


if __name__ == '__main__':
    main()