from .rpy_chrctr_obj import RenPy_Character_Object

class RenPy_Character_Data():
    def __init__(self):
        self.chrctr_objs: list[RenPy_Character_Object] = []
    
    def add_chrctr(self, obj: RenPy_Character_Object):
        self.chrctr_objs.append(obj)
    
    def sort_chrctrs(self):
        self.chrctr_objs.sort(key=lambda chrctr_obj : chrctr_obj.get_abbrev())
    
    def get_chrctrs(self):
        return self.chrctr_objs

    