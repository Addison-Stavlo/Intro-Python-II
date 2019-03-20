class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_pick_up(self):
        print(f'\nYou pick up item: {self.name}')

    def on_drop(self):
        print(f'\nYou drop item: {self.name}')
