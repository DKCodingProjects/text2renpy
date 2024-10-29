from .reader import Reader
from docx import Document
from src.misc.text_data import Text_Data

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

    def readchunk(self) -> tuple[list[Text_Data], dict]:
        try:
            # raise Exception('Docx_Reader \'readchunk\' is still in development! Download latest version or wait for update.')
            for paragraph in self.content:
                for run in paragraph.runs:
                    print(run.text)
                    print('has_bold = ',run.bold)
                    if run.bold:
                        print('  bold line = ', "{{b}}{0}{{/b}}".format(run.text))
                    print('has_italics = ',run.italic)
                    print('has_underlines = ',run.underline)
                    print('has_strikethrough = ',run.font.strike)
                    print('has_subscript = ',run.font.subscript)
                    print('has_superscript = ',run.font.superscript)
                    print('color = ',run.font.color.rgb)
                    print('has_size = ',run.font.size)
                    if run.font.size:
                        print('  size = ',run.font.size.pt)
            curr_text = ''
            curr_attrib = None
            self.is_eof = True
        except Exception as err:
            raise Exception('Something went wrong with Docx_Reader in method \'readchunk\'('+f"{type(err).__name__}: {err}"+')')
        return curr_text, curr_attrib