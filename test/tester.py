from src.read import *
from src.general.text_chunk import Text_Chunk
import os, sys

class Tester():
    def __init__(self):
        pass

    # def test_template() -> list[str, bool, str]:
    #     name = ''
    #     status = False
    #     msg = ''
    #     try:
    #         pass
    #     except Exception as err:
    #         msg = f"{type(err).__name__}: {err}"
    #     else:
    #         pass
    #     return name, status, msg
    
    # def test_raw_txt() -> list[str, bool, str]:
    #     name = 'Reading Screenplay TXT file using Raw_Reader'
    #     status = False
    #     msg = ''
    #     try:
    #         txt_file = os.path.join('test', 'test_screenplays', 'test_script.txt')
    #         read_txt = raw_reader.Raw_Reader(txt_file)
    #         read_txt.open()
    #         curr_line, curr_attrib = read_txt.readpart()
    #         while not read_txt.is_eof:
    #             curr_line, curr_attrib = read_txt.readpart()
    #     except Exception as err:
    #         msg = f"{err}"
    #     else:
    #         status = True 
    #         msg = 'Successfully read \'test_script.txt\' without issue.'
    #     return name, status, msg
    
    # def test_md_fountain() -> list[str, bool, str]:
    #     name = 'Reading Screenplay Fountain file using Raw_Reader'
    #     status = False
    #     msg = ''
    #     try:
    #         fountain_file = os.path.join('test', 'test_screenplays', 'test_script.fountain')
    #         read_fountain = md_reader.Markdown_Reader(fountain_file)
    #         read_fountain.open()
    #         curr_line, curr_attrib = read_fountain.readpart()
    #         while not read_fountain.is_eof:
    #             curr_line, curr_attrib = read_fountain.readpart()
    #     except Exception as err:
    #         msg = f"{err}"
    #     else:
    #         status = True 
    #         msg = 'Successfully read \'test_script.fountain\' without issue.'
    #     return name, status, msg
    
    # def test_xml_fdx() -> list[str, bool, str]:
    #     name = 'Reading Screenplay FDX file using Fdx_Reader'
    #     status = False
    #     msg = ''
    #     try:
    #         fdx_file = os.path.join('test', 'test_screenplays', 'test_script.fdx')
    #         read_fdx = fdx_reader.Fdx_Reader(fdx_file)
    #         read_fdx.open()
    #         curr_line, curr_attrib = read_fdx.readpart()
    #         while not read_fdx.is_eof:
    #             curr_line, curr_attrib = read_fdx.readpart()
    #     except Exception as err:
    #         msg = f"{err}"
    #     else:
    #         status = True
    #         msg = 'Successfully read \'test_script.fdx\' without issue.'
    #     return name, status, msg
    
    # def test_docx() -> list[str, bool, str]:
    #     name = 'Reading Screenplay DOCX file using Docx_Reader'
    #     status = False
    #     msg = ''
    #     try:
    #         docx_file = os.path.join('test', 'test_screenplays', 'test_script.docx')
    #         read_docx = docx_reader.Docx_Reader(docx_file)
    #         read_docx.open()
    #         curr_line, curr_attrib = read_docx.readpart()
    #         while not read_docx.is_eof:
    #             curr_line, curr_attrib = read_docx.readpart()
    #     except Exception as err:
    #         msg = f"{err}"
    #     else:
    #         status = True 
    #         msg = 'Successfully read \'test_script.docx\' without issue.'
    #     return name, status, msg
    
    # def print_test(name: str, status: bool, msg: str):
    #     status_cond = 'SUCCESS!' if status else 'Failure...'
    #     print_str = name+':\n  Status = '+status_cond+'\n  Message = \"'+msg+'\"'
    #     print(print_str)

    # def test_all():
    #     name, value, msg = Tester.test_raw_txt()
    #     Tester.print_test(name, value, msg)
    #     name, value, msg = Tester.test_md_fountain()
    #     Tester.print_test(name, value, msg)
    #     name, value, msg = Tester.test_xml_fdx()
    #     Tester.print_test(name, value, msg)
    #     name, value, msg = Tester.test_docx()
    #     Tester.print_test(name, value, msg)
