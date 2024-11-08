from .analyzer import Document_Analyzer
from src.read.docx_reader import Docx_Reader
from src.store.doc_metadata import Document_Metadata
from src.format.default.default_document import Default_Document
from src.enum.para_align_enum import Paragraph_Alignment

class Docx_Analyzer(Document_Analyzer):
    def __init__(self, read_file):
        super().__init__(read_file)

    def analyze_except(self, err):
        return super().analyze_except(err)

    def update_occurence(key: any, occurence_dict: dict) -> dict:
        if key in occurence_dict:
            occurence_dict[key] = occurence_dict[key] + 1
        else:
            occurence_dict[key] = 1
        return occurence_dict
    
    def get_max(occurence_dict: dict) -> any:
        max_key = None
        max_value = -1
        for key, value in occurence_dict.items():
            if value is None:
                continue
            elif value > max_value:
                max_key = key
                max_value = value
        return max_key

    def analyze(self) -> Document_Metadata:
        reader = Docx_Reader(self.file_name)
        reader.open()
        size_analysis = {}
        indent_analysis = {}
        alignment_analysis = {}
        while not reader.is_eof:
            curr_chunks, para_attribs = reader.readpart()
            for chunk in curr_chunks:
                Docx_Analyzer.update_occurence(chunk.get_size(), size_analysis)
            Docx_Analyzer.update_occurence(para_attribs.get_left_indent(), indent_analysis)
            Docx_Analyzer.update_occurence(para_attribs.get_alignment(), alignment_analysis)
        dominant_size = Docx_Analyzer.get_max(size_analysis)
        dominant_indent = Docx_Analyzer.get_max(indent_analysis)
        dominant_alignment = Docx_Analyzer.get_max(alignment_analysis)
        metadata = Document_Metadata(self.file_name)
        metadata.set_font_size(dominant_size 
                               if type(dominant_size) is float 
                               else Default_Document.font_size)
        metadata.set_left_indent(dominant_indent 
                                 if dominant_indent is float 
                                 else Default_Document.left_indent)
        metadata.set_alignment(dominant_alignment 
                               if (type(dominant_alignment) is Paragraph_Alignment 
                                   and dominant_alignment != Paragraph_Alignment.NONE) 
                               else Default_Document.alignment)
        return metadata