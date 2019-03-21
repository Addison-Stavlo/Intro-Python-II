# Implement a class to hold room information. This should have name and
# description attributes.

# making a change for initial push


class Room:
    def __init__(self, name, description, is_lit=True):
        self.name = name
        self.description = description
        self.list = []
        self.is_lit = is_lit

    def show_exits(self):
        directions = []
        if hasattr(self, 'n_to'):
            directions.append('North')
        if hasattr(self, 's_to'):
            directions.append('South')
        if hasattr(self, 'e_to'):
            directions.append('East')
        if hasattr(self, 'w_to'):
            directions.append('West')
        if len(directions) == 0:
            print(f'     You see no exit to this room!\n')
        elif len(directions) == 1:
            print(f'     You see an exit to the {directions[0]}\n')
        elif len(directions) == 2:
            print(
                f'     You see exits to the {directions[0]} and {directions[1]}\n')
        elif len(directions) == 3:
            print(
                f'     You see exits to the {directions[0]}, {directions[1]}, and {directions[2]}\n')
        else:
            print(f'     You see exits in all directions.\n')
