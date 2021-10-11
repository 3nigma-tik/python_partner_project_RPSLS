from players import Player


class AI(Player):
    def __init__(self):
        self.name = "Deep Blue"

    def pick_gesture(self):
        ai_gesture = Player.gesture
        import random
        robot_gesture = random.randint(ai_gesture)
        return robot_gesture
 
    
