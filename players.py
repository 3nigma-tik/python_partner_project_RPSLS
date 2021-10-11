from gestures import Gestures


class Player:
    def __init__(self, name, gesture):
        self.name = name
        self.gesture = ["rock", "paper", "scissors", "lizard", "spock"]
        self.available_gestures = [Gestures("rock"), Gestures("paper"), Gestures("scissors"), Gestures("lizard"), Gestures("spock")]
        self.chosen_gesture = Gestures("")
        self.score = 0


    def increase_score(self):
        self.score += 1

    def which_handsign(self, gesture):
        pick_gesture = int(gesture)
        print(pick_gesture)  

        
    def round_winner():
        pass

