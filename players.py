from gestures import Gestures



class Player:
    def __init__(self, name, gesture):
        self.name = name
        self.available_gestures = [Gestures("rock"), Gestures("paper"), Gestures("scissors"), Gestures("lizard"), Gestures("spock")]
        self.chosen_gesture = Gestures("")
        self.score = 0

     

    def increase_score(self):
        self.score += 1

    def which_handsign(self, chosen_gesture):
        pick_gesture = input(Gestures.chosen_gesture)
        print(pick_gesture)  

        
    def round_winner():
        pass

