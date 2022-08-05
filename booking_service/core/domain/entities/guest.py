from dataclasses import dataclass


@dataclass
class Guest:
    id: int
    name: str
    surname: str
    email: str
    
    def __init__(self, id, name, surname, email):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
