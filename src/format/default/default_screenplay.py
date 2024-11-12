from src.data.prog.enum.para_alignment import PARAGRAPH_ALIGNMENT

class Default_Screenplay:
    # Based on industry standards
    alignment = PARAGRAPH_ALIGNMENT.LEFT
    font_size: float = 12.0
    left_indent: float = 1.5 # for actions, headers, subheaders, sluglines, etc.
    right_indent: float = 1.0
    chrctr_indent: float = 3.5 # or Center-Alignment
    prnth_indent: float = 3.0 # or Center-Alignment
    dialog_indent: float = 2.5
    trnstn_indent: float = 6.0 # or Right-Alignment