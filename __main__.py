from src.args import *
from src.read import *
from src.translate import *
from test.tester import Tester
###############################
import dev.sandbox as dev
import docx
import os

def main():
    '''
    print('starting program...')
    argv = argv_parse.Argv_Parser()
    args = argv.parser.parse_args()
    arg_obj = args_obj.Args_Object()
    arg_obj.argparse_populate(args)
    arg_obj.print()
    '''
    Tester.test_all()
    nonetype = None
    if nonetype is None:
        print('True!')
    else:
        print('False')

if __name__ == '__main__':
    main()