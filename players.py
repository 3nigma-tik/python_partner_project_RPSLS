from gestures import Gestures

class Players:
    def __init__(self, name):
        self.available_gestures = [Gestures("rock"), Gestures("paper"), Gestures("scissors"), Gestures("lizard"), Gestures("spock")]
        self.chosen_gesture = Gestures("")
        self.name = name
        self.score = 0


    def increase_score(self):
        self.score += 1