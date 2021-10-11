from players import Player


class AI(Player):
    def __init__(self):
        self.name = "Deep Blue"

    def pick_gesture(self):
        ai_gesture = int(Player.available_gestures)
        import random
        robot_gesture = random.randint(ai_gesture)
        print(str(robot_gesture))
 
    pick_gesture("")
