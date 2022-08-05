from dataclasses import dataclass


@dataclass
class Room:
    id: int
    name: str
    level: str
    in_maintenance: bool

    def __init__(self, id, name, level, in_maintenance):
        self.id = id
        self.name = name
        self.level = level
        self.in_maintenance = in_maintenance
        
    def has_guest(self):
        # verificar se existem bookins abertos para esta room
        return self.guest is not None

    def is_available(self):
        return not self.has_guest() or not self.in_maintenance
