from src.data.prog.enum.para_alignment import PARAGRAPH_ALIGNMENT

class Default_Document:
    # informed by common best practices
    alignment = PARAGRAPH_ALIGNMENT.LEFT
    font_size: float = 11.0
    left_indent: float = 1.0
    right_indent: float = 1.0
    # most document properties (spacing, first line indentation, etc.) are irrelevant to this program