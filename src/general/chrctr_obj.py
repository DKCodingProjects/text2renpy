class RenPy_Character_Object:
    def __init__(self, name: str):
        self.name = name # name.strip().title()
        self.abbrev_name = name[0:1].lower() if len(name) >= 2 else (name[0]+name[0]).lower()
        self.sprites_used: list[str] = []

    def get_name(self):
        return self.name
    
    def set_name(self, new_name: str):
        self.name = new_name
        
    def get_abbrev(self):
        return self.abbrev_name
    
    def set_abbrev(self, new_abbrev: str):
        self.abbrev_name = new_abbrev

    def add_sprite(self, new_sprite: str):
        self.sprites_used.append(new_sprite)

    def find_sprite(self, sprite: str) -> bool:
        if sprite in self.sprites_used:
            return True
        else:
            return False
        
    def sort_sprites(self):
        self.sprites_used = self.sprites_used.sort()