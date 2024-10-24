from .reader import Reader
import xml.etree.ElementTree as et

class FDX_Reader(Reader):
    def __init__(self, read_file: str):
        super().__init__(read_file)

    def open(self):
        try:
            self.open_file = et.parse(self.file_name)
            self.content = self.open_file.getroot().find('Content')
            self.curr_index = 0
            self.max_index = len(self.content)
            '''
            for paragraph in self.content.iter('Paragraph'):
                print(paragraph.tag, paragraph.attrib, paragraph.find('Text').text)
            for i in range(0,self.max_index):
                print(self.content[i].tag, self.content[i].attrib)
                if (self.content[i].find('Text') is not None) and (self.content[i].tag == 'Paragraph'):
                    print(self.content[i].find('Text').text)
            '''
        except Exception as err:
            print('An error ocuured while parsing file \"'+self.file_name+'\"', err)
            exit()
    
    def processxml(self):
        pass

    def readline(self) -> tuple[str, dict]:
        try:
            curr_text = ''
            curr_attrib = None
            if self.curr_index < self.max_index:
                if self.content[self.curr_index].tag == 'Paragraph':
                    curr_paragraph = self.content[self.curr_index]
                    curr_attrib = {k.lower(): v.lower() for k, v in curr_paragraph.attrib.items()}
                    if self.content[self.curr_index].find('Text') is not None:
                        curr_text = curr_paragraph.find('Text').text
                self.curr_index += 1
        except Exception as err:
            print('Something went wrong with FDX_reader: ', err)
            exit()
        return curr_text, curr_attrib