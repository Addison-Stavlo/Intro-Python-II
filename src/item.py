from termcolor import colored


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_pick_up(self):
        print(
            colored(f'\n     You pick up item: {self.name}', 'yellow', attrs=['bold']))

    def on_drop(self):
        print(
            colored(f'\n     You drop item: {self.name}', 'yellow', attrs=['bold']))


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print(colored(f'\n     It is not wise to drop your source of light!',
                      'yellow', attrs=['bold']))
