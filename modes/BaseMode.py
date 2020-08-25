

class BaseMode:

    clacks = None
    size = None

    def __init__(self, clacks, size):
        self.clacks = clacks
        self.size = size

    def enter_screen(self):
        pass

    def exit_screen(self):
        pass

    def handle_event(self, event):
        pass

    def render(self, event):
        pass