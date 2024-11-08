from src.enum.para_align_enum import Paragraph_Alignment

class Default_Document:
    # informed by common best practices
    alignment = Paragraph_Alignment.LEFT
    font_size: float = 11.0
    left_indent: float = 1.0
    right_indent: float = 1.0
    # most document properties (spacing, first line indentation, etc.) are irrelevant to this program