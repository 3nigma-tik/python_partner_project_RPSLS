class Player:
    def __init__(self, name, gesture):
        self.name = name
        self.gesture = ["rock", "paper", "scissors", "lizard", "spock"]

    def display_greeting():
        return 

    def display_rules():
        rules = ["Rules:", "scissors cuts paper", "paper covers rock", "rock crushes scissors", "lizard easts paper", "paper disproves spock", "spock vaporizes rock", "lizard poisons spock", "scissors decapitate lizard", "spock smashes scissors"]
        print(*rules, sep = "\n")

    def pick_a_mode():
        mode_input = input("Pick 'PvP' or 'PvE'")
        return

    def which_handsign(self, gesture):
        pick_gesture = int(gesture)
        print(pick_gesture)  

        
    def round_winner():
        pass

    display_rules()