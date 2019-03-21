# Implement a class to hold room information. This should have name and
# description attributes.

# making a change for initial push
from termcolor import colored


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
            print(colored(f'     You see no exit to this room!\n',
                          'green', attrs=['bold']))
        elif len(directions) == 1:
            print(
                colored(f'     You see an exit to the {directions[0]}\n', 'green', attrs=['bold']))
        elif len(directions) == 2:
            print(colored(
                f'     You see exits to the {directions[0]} and {directions[1]}\n', 'green', attrs=['bold']))
        elif len(directions) == 3:
            print(colored(
                f'     You see exits to the {directions[0]}, {directions[1]}, and {directions[2]}\n', 'green', attrs=['bold']))
        else:
            print(colored(f'     You see exits in all directions.\n',
                          'green', attrs=['bold']))


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light
flickers in the distance, but there is no way 
across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", is_lit=False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely 
emptied by earlier adventurers. The only exit 
is to the south.""", is_lit=False),

    'traproom': Room("Trap Room", """The door slams behind you and you hear
the lock click as it shuts.  You see a shrine 
to the great goddess of the willows.  Maybe you 
should leave an offering...""", is_lit=False),

}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['narrow'].s_to = room['traproom']
