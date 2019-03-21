from termcolor import colored


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_pick_up(self):
        print(
            colored(f'\n     You pick up {type(self).__name__}: {self.name}', 'yellow', attrs=['bold']))

    def on_drop(self):
        print(
            colored(f'\n     You drop {type(self).__name__}: {self.name}', 'yellow', attrs=['bold']))


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print(colored(f'\n     It is not wise to drop your source of light!',
                      'yellow', attrs=['bold']))


class Treasure(Item):
    def __init__(self, name, value):
        self.description = 'This looks like it might be worth some gold!'
        self.value = value
        self.name = name

    def on_drop(self):
        print(
            colored(f"\n     You drop Treasure: {self.name}.  You don't like Treasure!?", 'yellow', attrs=['bold']))


class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage
