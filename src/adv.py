from room import Room
from player import Player
from item import Item
import os

# Setup Control Functions


def move_player(player, direction):
    if direction == 'N':
        if hasattr(player.location, 'n_to'):
            player.location = player.location.n_to
        else:
            print(
                f'\n\n--Error: There is no room North of {player.location.name}--')
            input("\npress 'Enter' to continue")
    elif direction == 'S':
        if hasattr(player.location, 's_to'):
            player.location = player.location.s_to
        else:
            print(
                f'\n\n--Error: There is no room South of {player.location.name}--')
            input("\npress 'Enter' to continue")
    elif direction == 'E':
        if hasattr(player.location, 'e_to'):
            player.location = player.location.e_to
        else:
            print(
                f'\n\n--Error: There is no room East of {player.location.name}--')
            input("\npress 'Enter' to continue")
    elif direction == 'W':
        if hasattr(player.location, 'w_to'):
            player.location = player.location.w_to
        else:
            print(
                f'\n\n--Error: There is no room West of {player.location.name}--')
            input("\npress 'Enter' to continue")
    else:
        print('this should not trigger...')
        input("\npress 'Enter' to continue")


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
        print(f'\n\n--Error: {item_name} does not exist in this room.--')
    input("\npress 'Enter' to continue")


def drop_item(player, item_name):
    for each_item in player.inventory:
        if each_item.name == item_name:
            player.location.list.append(each_item)
            player.inventory.remove(each_item)
            each_item.on_drop()
            break
    else:
        print(f'\n\n--Error: {item_name} does not exist in inventory.--')
    input("\npress 'Enter' to continue")


def show_inventory(player):
    print('\nInventory List:')
    for each_item in player.inventory:
        print(f'    {each_item.name}: {each_item.description}')
    input("\npress 'Enter' to continue")


def print_region(player):

    print(f'\n\n--Location: {player.location.name}--')
    print('    '+player.location.description, '\n')
    print('Visible Items:')

    for each in player.location.list:
        print('    '+each.name+': ', each.description)


def print_commands():
    print("\nEnter 'N', 'S', 'E', or 'W' to move.")
    print("Enter 'take' or 'get' + the item's name to pick up an item.")
    print("Enter 'drop' + the item's name to drop an item.")
    print("Enter 'i' or 'inventory' to view your inventory")
    print("Enter 'Q' to quit")
    global command
    command = input('\nWhat do you do?: ')
    handle_input(command)

# Setup main Loop Functions


def start_turn(player):
    # clear console first
    os.system('cls' if os.name == 'nt' else 'clear')
    print_region(player)


def get_input():
    global command
    command = input(
        "\nWhat do you do? (Enter 'help' for command list): ")


def handle_input(command):
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
        print('\n**You have ended the game.**\n')
    else:
        print('\nwhat command is this!?')
        input("\npress 'Enter' to continue")


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


# instantiate/initialize player, room items, and command
player = Player(room['outside'])
add_item(room['outside'], 'HealthGlobe', 'Glowey Globe of Shiny Red Stuffs')
add_item(room['outside'], 'Sign', 'Danger, Keep out!')
command = 1  # anything other than 'Q' to start main loop

# Main
while command != 'Q':
    start_turn(player)
    get_input()
    handle_input(command)
