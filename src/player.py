# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource


class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = []

    def move(self, direction):
        if direction == 'N':
            if hasattr(self.location, 'n_to'):
                self.location = self.location.n_to
            else:
                self.move_error('North')
        elif direction == 'S':
            if hasattr(self.location, 's_to'):
                self.location = self.location.s_to
            else:
                self.move_error('South')
        elif direction == 'E':
            if hasattr(self.location, 'e_to'):
                self.location = self.location.e_to
            else:
                self.move_error('East')
        elif direction == 'W':
            if hasattr(self.location, 'w_to'):
                self.location = self.location.w_to
            else:
                self.move_error('West')
        else:
            print('     this should not trigger...')
            input("\n     press 'Enter' to continue")

    def move_error(self, direction):
        print(
            f'\n\n     --Error: There is no room {direction} of {self.location.name}--')
        input("\n     press 'Enter' to continue")

    def pick_up_item(self, item_name):
        for item in self.location.list:
            if item.name == item_name:
                self.inventory.append(item)
                self.location.list.remove(item)
                item.on_pick_up()
                break
        else:
            print(
                f'\n\n     --Error: {item_name} does not exist in this room.--')
        input("\n     press 'Enter' to continue")

    def drop_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.location.list.append(item)
                self.inventory.remove(item)
                item.on_drop()
                break
        else:
            print(
                f'\n\n     --Error: {item_name} does not exist in inventory.--')
        input("\n     press 'Enter' to continue")

    def show_inventory(self):
        print('\n          Inventory List:')
        for item in self.inventory:
            print(f'              {item.name}: {item.description}')

    def can_see(self):
        # is room illuminated?
        if self.location.is_lit:
            return True
        # or does room list contain a light source?
        for item in self.location.list:
            if isinstance(item, LightSource):
                return True
        # or does self inventory contain a light source?
        for item in self.inventory:
            if isinstance(item, LightSource):
                return True
        return False
