from src.enum.para_align_enum import Paragraph_Alignment

class Default_Screenplay:
    # Based on industry standards
    alignment = Paragraph_Alignment.LEFT
    font_size: float = 12.0
    left_indent: float = 1.5 # for actions, headers, subheaders, sluglines, etc.
    right_indent: float = 1.0
    chrctr_indent: float = 3.5
    prnth_indent: float = 3.0
    dialog_indent: float = 2.5
    trnstn_indent: float = 6.0