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
        

    # def __init__(self):
    #     self.name = "Deep Blue"

    # def pick_gesture(self):
    #     ai_gesture = int(Player.available_gestures)
    #     import random
    #     robot_gesture = random.randint(ai_gesture)
    #     print(str(robot_gesture))
 
    # pick_gesture("")

