from src.args import *
from src.read import *
from src.translate import *
from test.tester import Tester
###############################
import dev.sandbox as dev

def main():
    '''
    print('starting program...')
    argv = argv_parse.Argv_Parser()
    args = argv.parser.parse_args()
    arg_obj = args_obj.Args_Object()
    arg_obj.argparse_populate(args)
    arg_obj.print()
    '''
    # print(type(reader_proxy.Reader_Proxy.get_reader('somefile.fdx')))
    Tester.test_all()

if __name__ == '__main__':
    main()