from room import Room, room
from player import Player
from item import Item, LightSource, Treasure, Weapon
import os
import textwrap
from termcolor import colored

# Setup Printing Functions


def add_item(room, item_name, item_description):
    room.list.append(Item(item_name, item_description))


def print_region(player):
    print(colored(
        f'\n\n     Location: {player.location.name}\n', 'green', attrs=['bold']))
    print(textwrap.indent(
        text=colored(f'     {player.location.description}\n', 'green', attrs=['bold']), prefix='          ', predicate=lambda line: True))
    player.location.show_exits()

    if len(player.location.list) > 0:
        print(colored('          Visible Items:',
                      'yellow', attrs=['bold']))
        for each in player.location.list:
            print(
                colored(f'              {each.name}: {each.description}', 'yellow', attrs=['bold']))


help_commands = colored("""
    -Move- Enter 'N', 'S', 'E', or 'W'.
    -Take Item- Enter 'take' or 'get' + the item's name
    -Drop Item- Enter 'drop' + the item's name.
    -Inventory- Enter 'i' or 'inventory'
    -Quit- Enter 'Q'""", 'red', attrs=['bold'])


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
        print(colored('\n\n    It is too dark to see anything.  Obtain a Light Source!',
                      'green', attrs=['bold']))


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
            print(colored(
                '\n     How can you take inventory in the dark!?', 'red', attrs=['bold']))
            input("\n     Press 'Enter' to continue.")
    elif lc_command == 'help':
        print_commands()
        get_input()
        handle_input()
    elif lc_command == 'q':
        print(colored('\n     **You have ended the game.**\n',
                      'red', attrs=['bold']))
        input("\n     press 'Enter' to continue")
    else:
        print(colored('\n     what command is this!?', 'red', attrs=['bold']))
        input("\n     press 'Enter' to continue")


# instantiate/initialize player, room items, and command
player = Player(room['outside'])
add_item(room['outside'], 'HealthGlobe', 'Glowey Globe of Shiny Red Stuffs')
add_item(room['outside'], 'Sign', 'Danger, Keep out!')
room['outside'].list.append(LightSource(
    'WillowWisp', 'A globe of shiny lights'))
room['traproom'].list.append(LightSource(
    'Torch', 'Fire strikes fear in the hearts of shadows'))
room['traproom'].list.append(Treasure('FineGemstone', 500))
room['traproom'].list.append(
    Weapon('Sword', 'A basic but effective looking blade.', 5))

command = ''  # anything other than 'q' to start main loop

# Main
while command.lower() != 'q':
    start_turn(player)
    get_input()
    handle_input()
