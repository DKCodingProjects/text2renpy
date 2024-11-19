from .analyzer import Analyzer
from src.read.docx_reader import Docx_Reader
from src.data.prog.build.doc_metadata import Document_Metadata
from src.format.default.default_document import Default_Document
from src.data.prog.enum.para_alignment import PARAGRAPH_ALIGNMENT

class Docx_Analyzer(Analyzer):
    def __init__(self, read_file):
        super().__init__(read_file)
    
    def print(self):
        return super().print(self)

    def _analyze_except(self, err):
        return super()._analyze_except(err)

    def _update_occurence(key: any, occurence_dict: dict) -> dict:
        if key in occurence_dict:
            occurence_dict[key] = occurence_dict[key] + 1
        else:
            occurence_dict[key] = 1
        return occurence_dict
    
    def _get_max(occurence_dict: dict) -> any:
        max_key = None
        max_value = -1
        for key, value in occurence_dict.items():
            if value is None:
                continue
            elif value > max_value:
                max_key = key
                max_value = value
        return max_key
    
    def _find_default_size(self, document):
        if(document != None and
        document.styles != None and
        document.styles.element != None):
            styles_elem = document.styles.element
            # print(et.tostring(styles_elem))

            default_LXML = styles_elem.xpath('w:docDefaults/w:rPrDefault')
            if(len(default_LXML) != 0 and
                len(default_LXML[0]) != 0):

                # https://github.com/python-openxml/python-docx/blob/master/docx/oxml/text/font.py#L52
                run = default_LXML[0][0] # Should be a type CT_RPr

                if(run.sz_val):
                    return run.sz_val.pt

        return -1

    def analyze(self):
        reader = Docx_Reader(self.file_name)
        reader.open()
        size_analysis = {}
        indent_analysis = {}
        alignment_analysis = {}
        while not reader.is_eof:
            curr_chunks, para_attribs = reader.readpart()
            for chunk in curr_chunks:
                Docx_Analyzer._update_occurence(chunk.get_size(), size_analysis)
            Docx_Analyzer._update_occurence(para_attribs.get_left_indent(), indent_analysis)
            Docx_Analyzer._update_occurence(para_attribs.get_alignment(), alignment_analysis)
        dom_size = Docx_Analyzer._get_max(size_analysis)
        dom_indent = Docx_Analyzer._get_max(indent_analysis)
        dom_alignment = Docx_Analyzer._get_max(alignment_analysis)
        metadata = Document_Metadata(self.file_name)
        metadata.set_font_size(dom_size
                               if type(dom_size) is float 
                               else Default_Document.font_size)
        metadata.set_left_indent(dom_indent
                                 if dom_indent is float 
                                 else Default_Document.left_indent)
        metadata.set_alignment(dom_alignment
                               if (type(dom_alignment) is PARAGRAPH_ALIGNMENT 
                                   and dom_alignment != PARAGRAPH_ALIGNMENT.NONE) 
                               else Default_Document.alignment)
        return metadata