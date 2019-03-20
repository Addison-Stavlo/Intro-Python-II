from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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


def move_player(player, direction):
    if direction == 'N':
        if hasattr(player.location, 'n_to'):
            player.location = player.location.n_to
        else:
            print(
                f'\n\n--Error: There is no room North of {player.location.name}--')
    if direction == 'S':
        if hasattr(player.location, 's_to'):
            player.location = player.location.s_to
        else:
            print(
                f'\n\n--Error: There is no room South of {player.location.name}--')
    if direction == 'E':
        if hasattr(player.location, 'e_to'):
            player.location = player.location.e_to
        else:
            print(
                f'\n\n--Error: There is no room East of {player.location.name}--')
    if direction == 'W':
        if hasattr(player.location, 'w_to'):
            player.location = player.location.w_to
        else:
            print(
                f'\n\n--Error: There is no room West of {player.location.name}--')


def add_item(room, item_name, item_description):
    room.list.append(Item(item_name, item_description))


add_item(room['outside'], 'HealthGlobe', 'Glowey Globe of Shiny Red Stuffs')
add_item(room['outside'], 'Sign', 'Danger, Keep out!')


def pick_up_item(player, item_name):
    for each_item in player.location.list:
        if each_item.name == item_name:
            player.inventory.append(each_item)
            player.location.list.remove(each_item)
            break
    else:
        print(f'\n\n--Error: {item_name} does not exist in this room.--')


def drop_item(player, item_name):
    for each_item in player.inventory:
        if each_item.name == item_name:
            player.location.list.append(each_item)
            player.inventory.remove(each_item)
            break
    else:
        print(f'\n\n--Error: {item_name} does not exist in inventory.--')


# Main
#
# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
command = 1

while command != 'Q':
    print(f'\n\nLocation: {player.location.name}\n')
    print(player.location.description, '\n')
    print('Visible Items:')

    for each in player.location.list:
        print('    '+each.name+': ', each.description)

    command = input(
        '\nWhat do you do!? \nEnter N,S,E, or W to move. Q to quit: ')

    if command == 'N' \
            or command == 'S' \
            or command == 'E' \
            or command == 'W':
        move_player(player, command)
    elif command.startswith('take') or command.startswith('get'):
        item_name = command.split(' ')[1]
        pick_up_item(player, item_name)
    elif command.startswith('drop'):
        item_name = command.split(' ')[1]
        drop_item(player, item_name)
    else:
        print('what command is this!?')
