import re
from typing import Optional

class TextChunk:
    def __init__(self, text: str):
        self._text = text
        self._has_style = False
        self._bold: Optional[bool] = None
        self._italic: Optional[bool] = None
        self._underline: Optional[bool] = None
        self._strike: Optional[bool] = None
        self._color: Optional[str] = None
        self._size: Optional[float] = None

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value

    @property
    def has_style(self) -> bool:
        return self._has_style

    @property
    def bold(self) -> Optional[bool]:
        return self._bold

    @bold.setter
    def bold(self, value: Optional[bool]) -> None:
        self._validate_bool(value)
        self._bold = value
        self._update_style()

    @property
    def italic(self) -> Optional[bool]:
        return self._italic

    @italic.setter
    def italic(self, value: Optional[bool]) -> None:
        self._validate_bool(value)
        self._italic = value
        self._update_style()

    @property
    def underline(self) -> Optional[bool]:
        return self._underline

    @underline.setter
    def underline(self, value: Optional[bool]) -> None:
        self._validate_bool(value)
        self._underline = value
        self._update_style()

    @property
    def strike(self) -> Optional[bool]:
        return self._strike

    @strike.setter
    def strike(self, value: Optional[bool]) -> None:
        self._validate_bool(value)
        self._strike = value
        self._update_style()

    @property
    def color(self) -> Optional[str]:
        return self._color

    @color.setter
    def color(self, value: Optional[str]) -> None:
        if value is not None:
            self._validate_hex_color(value)
        self._color = value
        self._update_style()

    @property
    def size(self) -> Optional[float]:
        return self._size

    @size.setter
    def size(self, value: Optional[float]) -> None:
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(f"Expected float or int for size, got {type(value).__name__}")
        self._size = value
        self._update_style()

    def _validate_bool(self, value: Optional[bool]) -> None:
        if value is not None and not isinstance(value, bool):
            raise TypeError(f"Expected bool or None, got {type(value).__name__}")

    def _validate_hex_color(self, value: str) -> None:
        if not re.match(r'^[0-9A-Fa-f]{3,8}$', value):
            raise ValueError(f"Invalid hex color format: {value}")

    def _update_style(self) -> None:
        self._has_style = any(v is not None for v in [self._bold, self._italic, self._underline, self._strike, self._color, self._size])
