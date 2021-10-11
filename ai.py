from players import Player


class AI(Player):
    def __init__(self, name):
        self.name = "Deep Blue"

    def pick_gesture(self):
        gesture = ["rock", "paper", "scissors", "lizard", "spock"]
        import random
        self.gesture = random.randint(gesture)
        
    pick_gesture()
