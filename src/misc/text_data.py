class Text_Data():
    def __init__(self, text: str, attrib: dict):
        self.text = text
        self.attrib = attrib

    def get_text(self):
        return self.text
    
    def get_attrib(self):
        return self.attrib