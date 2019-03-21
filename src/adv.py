from room import Room
from player import Player
from item import Item, LightSource
import os

import textwrap

# Setup Printing Functions


def add_item(room, item_name, item_description):
    room.list.append(Item(item_name, item_description))


def print_region(player):
    print(f'\n\n     Location: {player.location.name}\n')
    print(textwrap.indent(
        text=f'     {player.location.description}\n', prefix='          ', predicate=lambda line: True))
    player.location.show_exits()
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


# Setup main Loop Functions


def start_turn(player):
    # clear console first
    os.system('cls' if os.name == 'nt' else 'clear')
    if player.determine_sight():
        print_region(player)
    else:
        print('    It is too dark to see anything.  Obtain a Light Source!')


def get_input():
    global command
    command = input(
        "\n     What do you do? (Enter 'help' for command list): ")


def handle_input():
    global command
    lc_command = command.lower()
    if lc_command == 'n' \
            or lc_command == 's' \
            or lc_command == 'e' \
            or lc_command == 'w':
        player.move(lc_command)
    elif lc_command.startswith('take') or lc_command.startswith('get'):
        item_name = command.split(' ')[1]
        player.pick_up_item(item_name)
    elif lc_command.startswith('drop'):
        item_name = command.split(' ')[1]
        player.drop_item(item_name)
    elif lc_command == 'i' or lc_command == 'inventory':
        if player.can_see:
            player.show_inventory()
            get_input()
            handle_input()
        else:
            print('\n     How can you take inventory in the dark!?')
            input("\n     Press 'Enter' to continue.")
    elif lc_command == 'help':
        print_commands()
        get_input()
        handle_input()
    elif lc_command == 'q':
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

command = ''  # anything other than 'q' to start main loop

# Main
while command.lower() != 'q':
    start_turn(player)
    get_input()
    handle_input()
