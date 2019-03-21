from room import Room
from player import Player
from item import Item, LightSource
import os

import textwrap

# Setup Control Functions


def move_player(player, direction):
    if direction == 'N':
        if hasattr(player.location, 'n_to'):
            player.location = player.location.n_to
        else:
            move_error(player, 'North')
    elif direction == 'S':
        if hasattr(player.location, 's_to'):
            player.location = player.location.s_to
        else:
            move_error(player, 'South')
    elif direction == 'E':
        if hasattr(player.location, 'e_to'):
            player.location = player.location.e_to
        else:
            move_error(player, 'East')
    elif direction == 'W':
        if hasattr(player.location, 'w_to'):
            player.location = player.location.w_to
        else:
            move_error(player, 'West')
    else:
        print('     this should not trigger...')
        input("\n     press 'Enter' to continue")


def move_error(player, direction):
    print(
        f'\n\n     --Error: There is no room {direction} of {player.location.name}--')
    input("\n     press 'Enter' to continue")


def add_item(room, item_name, item_description):
    room.list.append(Item(item_name, item_description))


def pick_up_item(player, item_name):
    for each_item in player.location.list:
        if each_item.name == item_name:
            player.inventory.append(each_item)
            player.location.list.remove(each_item)
            each_item.on_pick_up()
            break
    else:
        print(f'\n\n     --Error: {item_name} does not exist in this room.--')
    input("\n     press 'Enter' to continue")


def drop_item(player, item_name):
    for each_item in player.inventory:
        if each_item.name == item_name:
            player.location.list.append(each_item)
            player.inventory.remove(each_item)
            each_item.on_drop()
            break
    else:
        print(f'\n\n     --Error: {item_name} does not exist in inventory.--')
    input("\n     press 'Enter' to continue")


def show_inventory(player):
    print('\n          Inventory List:')
    for each_item in player.inventory:
        print(f'              {each_item.name}: {each_item.description}')
    get_input()
    handle_input()


def print_region(player):
    print(f'\n\n     Location: {player.location.name}\n')
    print(textwrap.indent(
        text=f'     {player.location.description}\n', prefix='          ', predicate=lambda line: True))
    print('          Visible Items:')
    for each in player.location.list:
        print('              '+each.name+': ', each.description)


help_commands = """
    -Move- Enter 'N', 'S', 'E', or 'W'.
    -Take Item- Enter 'take' or 'get' + the item's name
    -Drop Item- Enter 'drop' + the item's name.
    -Inventory- Enter 'i' or 'inventory'
    -Quit- Enter 'Q'"""


def print_commands():
    print(textwrap.indent(text=help_commands,
                          prefix='      ', predicate=lambda line: True))
    get_input()
    handle_input()


def can_see(player):
    # is room illuminated?
    if player.location.is_lit:
        return True
    # or does room list contain a light source?
    for item in player.location.list:
        if isinstance(item, LightSource):
            return True
    # or does player inventory contain a light source?
    for item in player.inventory:
        if isinstance(item, LightSource):
            return True
    return False

# Setup main Loop Functions


def start_turn(player):
    # clear console first
    os.system('cls' if os.name == 'nt' else 'clear')
    if can_see(player):
        print_region(player)
    else:
        print('    It is too dark to see anything.  Obtain a Light Source!')


def get_input():
    global command
    command = input(
        "\n     What do you do? (Enter 'help' for command list): ")


def handle_input():
    global command
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
    elif command == 'i' or command == 'inventory':
        show_inventory(player)
    elif command == 'help':
        print_commands()
    elif command == 'Q':
        print('\n     **You have ended the game.**\n')
    else:
        print('\n     what command is this!?')
        input("\n     press 'Enter' to continue")


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
to north. The smell of gold permeates the air.""", is_lit=False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", is_lit=False),
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


# instantiate/initialize player, room items, and command
player = Player(room['outside'])
add_item(room['outside'], 'HealthGlobe', 'Glowey Globe of Shiny Red Stuffs')
add_item(room['outside'], 'Sign', 'Danger, Keep out!')
# add lightsource to first room object list (add_item was made for top-level item class)
room['outside'].list.append(LightSource(
    'WillowWisp', 'A globe of shiny lights'))

command = 1  # anything other than 'Q' to start main loop

# Main
while command != 'Q':
    start_turn(player)
    get_input()
    handle_input()
