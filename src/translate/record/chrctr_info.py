class Character_Information:
    def __init__(self, name: str):
        self.name = name
        self.prnths: list[str] = []
        self.lines_spoken: int = 0

    def get_name(self):
        return self.name