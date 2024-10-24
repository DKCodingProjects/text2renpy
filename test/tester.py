from src.read import *
import os, sys

class Tester():

    def test_template() -> list[str, bool, str]:
        name = ''
        status = False
        msg = ''
        try:
            pass
        except Exception as err:
            msg = f"{type(err).__name__}: {err}"
        else:
            pass
        return name, status, msg
    
    def test_raw_txt() -> list[str, bool, str]:
        name = 'Reading Screenplay TXT file using Raw_Reader'
        status = False
        msg = ''
        try:
            txt_file = os.path.join('test', 'test_screenplays', 'test_script.txt')
            read_txt = raw_reader.Raw_Reader(txt_file)
            read_txt.open()
            curr_line, curr_attrib = read_txt.readline()
            while curr_line or curr_attrib:
                curr_line, curr_attrib = read_txt.readline()
        except Exception as err:
            msg = f"{type(err).__name__}: {err}"
        else:
            status = True 
            msg = 'Successfully read \'test_script.txt\' without issue.'
        return name, status, msg
    
    def test_xml_fdx() -> list[str, bool, str]:
        name = 'Reading Screenplay FDX file using FDX_Reader'
        status = False
        msg = ''
        try:
            fdx_file = os.path.join('test', 'test_screenplays', 'test_script.fdx')
            read_fdx = fdx_reader.FDX_Reader(fdx_file)
            read_fdx.open()
            curr_line, curr_attrib = read_fdx.readline()
            while curr_line or curr_attrib:
                curr_line, curr_attrib = read_fdx.readline()
        except Exception as err:
            msg = f"{type(err).__name__}: {err}"
        else:
            status = True
            msg = 'Successfully read \'test_script.fdx\' without issue.'
        return name, status, msg
    
    def print_test(name: str, status: bool, msg: str):
        status_cond = 'SUCCESS!' if status else 'Failure...'
        print_str = name+':\n  Status = '+status_cond+'\n  Message = \"'+msg+'\"'
        print(print_str)

    def test_all():
        name, value, msg = Tester.test_raw_txt()
        Tester.print_test(name, value, msg)
        name, value, msg = Tester.test_xml_fdx()
        Tester.print_test(name, value, msg)
