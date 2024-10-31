import re

class Text_Chunk():
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
            raise TypeError('value \"{0}\" passed to the {1} method in Text_Chunk isn\'t of type \'bool\''.format(value, method))
        else:
            pass # do nothing
    
    def set_style(self, value: bool):
        Text_Chunk.test_bool('set_style', value)
        self.has_style = value
    
    def set_bold(self, value: bool):
        Text_Chunk.test_bool('set_bold', value)
        if value: self.set_style(True)
        self.bold = value
    
    def is_bold(self) -> bool:
        return self.bold
    
    def set_italic(self, value: bool):
        Text_Chunk.test_bool('set_italic', value)
        if value: self.set_style(True)
        self.italic = value
    
    def is_italic(self) -> bool:
        return self.italic
    
    def set_underline(self, value: bool):
        Text_Chunk.test_bool('set_underline', value)
        if value: self.set_style(True)
        self.underline = value
    
    def is_underline(self) -> bool:
        return self.underline
    
    def set_strike(self, value: bool):
        Text_Chunk.test_bool('set_strike', value)
        if value: self.set_style(True)
        self.strike = value
    
    def is_strike(self) -> bool:
        return self.strike
    
    def set_color(self, value: str):
        if value is None:
            pass
        elif type(value) is not str:
            raise TypeError('Value {0} passed to Text_Chunk method \'set_color\' is not of type \'str\''.format(value))
        elif not re.match(r'^[0-9A-Fa-f]{3,8}$', value):
            raise TypeError('String \"{0}\" passed to Text_Chunk method \'set_color\' does not match desired hexadecimal format'.format(value))
        if value: self.set_style(True)
        self.color = value
    
    def get_color(self) -> str:
        return self.color
    
    def set_size(self, value):
        if value is None:
            pass
        elif type(value) is float:
            self.size = value
            if value > 0.0: self.set_style(True)
        else:
            raise TypeError('Value {0} passed to Text_Chunk method \'set_size\' is not of type \'float\''.format(value))
    
    def get_size(self) -> float:
        return self.size