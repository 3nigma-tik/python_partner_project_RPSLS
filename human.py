from players import Player


class Human(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def pick_gesture(self):
        print(self.name+" Type a gesture")
        for gesture in self.available_gestures:
            print(gesture.gesture_type)

        return input('')