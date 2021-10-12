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
        self.choice_validator()

    def choice_validator(self):
        validEntry = 1
        while validEntry != 0:
            userEntry = input()
            for each in self.available_gestures:
                if userEntry == each.gesture_type:
                    self.chosen_gesture = each
                    validEntry = 0
                    break
            if validEntry != 0:
                print("Invalid entry, try again!")