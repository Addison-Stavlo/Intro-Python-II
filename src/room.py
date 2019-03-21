# Implement a class to hold room information. This should have name and
# description attributes.

# making a change for initial push


class Room:
    def __init__(self, name, description, is_lit=True):
        self.name = name
        self.description = description
        self.list = []
        self.is_lit = is_lit
