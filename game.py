from tkinter import *

class Game:
    def __init__(self):
        pass

    def run_game(self):
        self.display_rules()
        self.display_welcome()
        self.play()
        self.display_winner()

    def display_welcome(btn):
        user_choice = input("Choose a mode:", "1: PvP", "2: PvE",  "3: Demo Mode")
        print(*user_choice, sep = "\n")
        

    def display_rules(self):
        rules = ["Rules:", "scissors cuts paper", "paper covers rock", "rock crushes scissors", "lizard easts paper", "paper disproves spock", "spock vaporizes rock", "lizard poisons spock", "scissors decapitate lizard", "spock smashes scissors"]
        print(*rules, sep = "\n")

    def play(self):
        pass

    def display_winner(self):   
        pass

        

    