
class Screenplay_Tracker:
    def __init__(self):
        self.curr_spkr: str = ''
        self.curr_prnth: str = ''
        self.curr_trnstn: str = ''
        self.curr_scene: str = ''

    def set_spkr(self, speaker: str):
        self.curr_spkr: str = speaker

    def get_spkr(self):
        return self.curr_spkr
    
    def set_prnth(self, parenthetical: str):
        self.curr_prnth = parenthetical

    def get_prnth(self):
        return self.curr_prnth

    def reset_spkr(self):
        self.curr_spkr: str = ''
        self.curr_prnth: str = ''

    def set_trnstn(self, transition: str):
        self.curr_trnstn = transition

    def get_trnstn(self):
        return self.curr_trnstn
    
    def set_scene(self, scene: str):
        self.curr_scene = scene

    def get_scene(self):
        return self.curr_scene
