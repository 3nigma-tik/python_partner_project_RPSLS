

class Gestures:
    def __init__(self, gesture_type):
        self.gesture_type = gesture_type
        self.defeats = []
        self.track_defeats()

    def track_defeats(self):
        if self.gesture_type == "rock":
            self.defeats.append("scissors")
            self.defeats.append("lizard")
        elif self.gesture_type == "paper":
            self.defeats.append("rock")
            self.defeats.append("spock")
        elif self.gesture_type == "scissors":
            self.defeats.append("paper")
            self.defeats.append("lizard")
        elif self.gesture_type == "lizard":
            self.defeats.append("paper")
            self.defeats.append("spock")
        elif self.gesture_type == "spock":
            self.defeats.append("scissors")
            self.defeats.append("rock")