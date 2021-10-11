from players import Players


class AI(Players):
    def __init__(self, name):
        self.name = name

    def pick_gesture(self):
        import random
        self.gesture = random.randint(gesture)

