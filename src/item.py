class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_pick_up(self):
        print(f'\n     You pick up item: {self.name}')

    def on_drop(self):
        print(f'\n     You drop item: {self.name}')


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print(f'\n     It is not wise to drop your source of light!')
