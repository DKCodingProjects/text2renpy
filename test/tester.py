from src.read import *
import os

class Tester():
    
    def test_raw_txt() -> list[bool, str]:
        try:
            txt_file = os.path.join('tests', 'test_screenplays', 'test_script.txt')
            read_txt = raw_reader.Raw_Reader(txt_file)
            read_txt.open()
            curr_line = read_txt.read()
            while curr_line:
                curr_line = read_txt.read()
        except:
            return False, 'Something went wrong with test_txt in Tester!'
        else:
            return True, 'Test \'test_raw_txt\' succeded!'
        
    def fail_raw_txt() -> list[bool, str]:
        try:
            txt_file = os.path.join('tests', 'test_screenplays', 'no_such_thing.txt')
            read_txt = raw_reader.Raw_Reader(txt_file)
            read_txt.open()
            curr_line = read_txt.read()
            while curr_line:
                curr_line = read_txt.read()
        except:
            return True, 'Test \'fail_raw_txt\' succeded!'
        else:
            return False, 'Something went wrong with test_txt in Tester!'
