# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource
from termcolor import colored
from room import room
# from adv import room


class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = []
        self.can_see = False

    def move(self, direction):
        if direction == 'n':
            if hasattr(self.location, 'n_to'):
                self.location = self.location.n_to
            else:
                self.move_error('North')
        elif direction == 's':
            if hasattr(self.location, 's_to'):
                self.location = self.location.s_to
            else:
                self.move_error('South')
        elif direction == 'e':
            if hasattr(self.location, 'e_to'):
                self.location = self.location.e_to
            else:
                self.move_error('East')
        elif direction == 'w':
            if hasattr(self.location, 'w_to'):
                self.location = self.location.w_to
            else:
                self.move_error('West')
        else:
            print('     this should not trigger...')
            input("\n     press 'Enter' to continue")

    def move_error(self, direction):
        print(colored(
            f'\n\n     --Error: There is no room {direction} of {self.location.name}--', 'red', attrs=['bold']))
        input("\n     press 'Enter' to continue")

    def determine_sight(self):
        # is room illuminated?
        if self.location.is_lit:
            self.can_see = True
            return True
        # or does room list contain a light source?
        for item in self.location.list:
            if isinstance(item, LightSource):
                self.can_see = True
                return True
        # or does self inventory contain a light source?
        for item in self.inventory:
            if isinstance(item, LightSource):
                self.can_see = True
                return True
        self.can_see = False
        return False

    def try_to_see(self):
        if self.can_see:
            return True
        else:
            print(colored('\n     Good luck finding that in the dark!',
                          'red', attrs=['bold']))
            input("\n     Press 'Enter' to continue.")

    def pick_up_item(self, item_name):
        if self.try_to_see():
            for item in self.location.list:
                if item.name.lower() == item_name.lower():
                    self.inventory.append(item)
                    self.location.list.remove(item)
                    item.on_pick_up()
                    break
            else:
                print(colored(
                    f'\n\n     --Error: "{item_name}" does not exist in this room.--', 'red', attrs=['bold']))
            input("\n     press 'Enter' to continue")

    def drop_item(self, item_name):
        if self.try_to_see():
            for item in self.inventory:
                if item.name.lower() == item_name.lower():
                    self.location.list.append(item)
                    self.inventory.remove(item)
                    item.on_drop()
                    self.on_drop_event_trigger(item.name)
                    break
            else:
                print(colored(
                    f'\n\n     --Error: "{item_name}" does not exist in inventory.--', 'red', attrs=['bold']))
            input("\n     press 'Enter' to continue")

    def show_inventory(self):
        print(colored('\n          Inventory List:', 'yellow', attrs=['bold']))
        for item in self.inventory:
            print(
                colored(f'              {item.name}: {item.description}', 'yellow', attrs=['bold']))

    def on_drop_event_trigger(self, item_name):
        if self.location.name == 'Trap Room' and item_name.lower() == 'willowwisp':
            self.location.n_to = room['narrow']
            room['traproom'].description = """Thankfully you unlocked this trap already."""
            print(colored(f'\n     You hear the door behind you open.',
                          'yellow', attrs=['bold']))
