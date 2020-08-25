

class Clacks:

    custom_events = None # This is dictionary of custom events

    alive = None

    clock = None

    def __init__(self):
        self.custom_events = {
            "MESSAGE":None,
            "RESUME": None
        }

        self.alive = True