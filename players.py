from gestures import Gestures


class Player:
    def __init__(self, name):
        self.name = name
        self.gesture = ["rock", "paper", "scissors", "lizard", "spock"]
        self.available_gestures = [Gestures("rock"), Gestures("paper"), Gestures("scissors"), Gestures("lizard"), Gestures("spock")]
        self.chosen_gesture = Gestures("")
        self.score = 0


    def increase_score(self):
        self.score += 1

    def display_greeting():
        return 

    def pick_a_mode():
        mode_input = input("Pick 'PvP' or 'PvE'")
        return

    def which_handsign(self, gesture):
        pick_gesture = int(gesture)
        print(pick_gesture)  

        
    def round_winner():
        pass

