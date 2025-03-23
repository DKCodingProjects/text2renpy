class RenPy_Character_Object:
    def __init__(self, name: str, abbrev_name: str, obj_str: str = ''):
        self.name = name
        self.abbrev_name = abbrev_name
        self.obj_str = obj_str
        self.sprites: list[str] = []

    def get_name(self):
        return self.name
        
    def get_abbrev(self):
        return self.abbrev_name
    
    def has_obj(self) -> bool:
        if self.obj_str:
            return True
        else:
            return False
    
    def get_obj(self):
        return self.obj_str

    def add_sprite(self, new_sprite: str):
        self.sprites.append(new_sprite)

    def find_sprite(self, sprite: str) -> bool:
        if sprite in self.sprites:
            return True
        else:
            return False
        
    def sort_sprites(self):
        self.sprites = self.sprites.sort()