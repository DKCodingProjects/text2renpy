from .reader import Reader
from docx import Document
from src.misc.text_chunk_data import Text_Chunk_Data

class Docx_Reader(Reader):
    def __init__(self, read_file):
        super().__init__(read_file)
    
    def lowercase_dict(self, dict):
        return super().lowercase_dict(dict)

    def open(self):
        try:
            self.open_file = Document(self.file_name)
            self.content = self.open_file.paragraphs
        except Exception as err:
            raise Exception('An error ocuured while opening document \''+self.file_name+'\' ('+f"{type(err).__name__}: {err}"+')')

    def readpart(self) -> tuple[list[Text_Chunk_Data], dict]:
        try:
            docx_record = open('output.txt', 'w')
            style = self.open_file.styles['normal']
            print(style.font.size)
            font = style.font
            # raise Exception('Docx_Reader \'readpart\' is still in development! Download latest version or wait for update.')
            for paragraph in self.content:
                for run in paragraph.runs:
                    if run.text.strip() != '':
                        docx_record.write(run.text+'\n')
                        docx_record.write('has_bold = '+str(run.bold)+'\n')
                        docx_record.write('has_italics = '+str(run.italic)+'\n')
                        docx_record.write('has_underlines = '+str(run.underline)+'\n')
                        docx_record.write('has_strikethrough = '+str(run.font.strike)+'\n')
                        docx_record.write('has_subscript = '+str(run.font.subscript)+'\n')
                        docx_record.write('has_superscript = '+str(run.font.superscript)+'\n')
                        if run.font.color and run.font.color.rgb:
                            docx_record.write('color = '+str(run.font.color.rgb)+'\n')
                        docx_record.write('has_size = '+str(run.font.size)+'\n')
            curr_text = ''
            curr_attrib = None
            self.is_eof = True
        except Exception as err:
            raise Exception('Something went wrong with Docx_Reader in method \'readpart\'('+f"{type(err).__name__}: {err}"+')')
        return curr_text, curr_attrib