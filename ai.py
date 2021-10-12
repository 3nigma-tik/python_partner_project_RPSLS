from players import Player
import random

class AI(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def pick_gesture(self):
        gesture = ["rock", "paper", "scissors", "lizard", "spock"]
        index = random.randint(0,4)
        print(f"{self.name} pick {gesture[index]}")
        return gesture[index]
        
