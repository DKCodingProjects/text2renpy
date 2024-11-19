from .chrctr_info import Character_Information

class Screenplay_Data:
    def __init__(self):
        self.characters: list[Character_Information] = []
        self.headers: list[str] = []

        self.curr_spkr: str = None
        self.curr_prnth: str = None
        self.curr_trnstn: str = None
        self.curr_scene: str = None

    def _sort_chrctr_helper(chrctr_info: Character_Information) -> str:
        return chrctr_info.get_name()
    
    def sort_characters(self):
        self.characters.sort(key=Screenplay_Data._sort_chrctr_helper)
