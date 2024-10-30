import re

class Text_Chunk_Data():
    def __init__(self, text: str):
        self.text = text
        self.bold: bool = None
        self.italic: bool = None
        self.underline: bool = None
        self.strike: bool = None
        self.color: str = None
        self.size: float = None
        self.has_style = False # set when any other class variable is set to a truthful value

    def set_text(self, text: str):
        self.text = text
    
    def get_text(self):
        return self.text
    
    def test_bool(method: str, value):
        if type(value) is not bool and value is not None:
            raise TypeError('value \"{0}\" passed to the {1} method in Text_Chunk_Data isn\'t of type \'bool\''.format(value, method))
        else:
            pass # do nothing
    
    def set_style(self, value: bool):
        Text_Chunk_Data.test_bool('set_style', value)
        self.has_style = value
    
    def set_bold(self, value: bool):
        Text_Chunk_Data.test_bool('set_bold', value)
        if value: self.set_style(True)
        self.bold = value
    
    def is_bold(self):
        return self.bold
    
    def set_italic(self, value: bool):
        Text_Chunk_Data.test_bool('set_italic', value)
        if value: self.set_style(True)
        self.italic = value
    
    def is_italic(self):
        return self.italic
    
    def set_underline(self, value: bool):
        Text_Chunk_Data.test_bool('set_underline', value)
        if value: self.set_style(True)
        self.underline = value
    
    def is_underline(self):
        return self.underline
    
    def set_strike(self, value: bool):
        Text_Chunk_Data.test_bool('set_strike', value)
        if value: self.set_style(True)
        self.strike = value
    
    def is_strike(self):
        return self.strike
    
    def set_color(self, value: str):
        if type(value) is not str or not re.match(r'^[0-9A-Fa-f]{3,8}$', value):
            raise Exception('String \"{0}\" passed to set_color does not match desired hexadecimal format'.format(value))
        if value: self.set_style(True)
        self.color = value
    
    def get_color(self):
        return self.color
    
    def set_size(self, value: float):
        if type(value) is float:
            self.size = value
            if value: self.set_style(True)
        else:
            try:
                self.size = float(value)
                if value: self.set_style(True)
            except Exception as err:
                raise TypeError(err)
    
    def get_size(self):
        return self.size
    
    '''
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
    '''