

from players import Player
from human import Human
from ai import AI 
import random
from tkinter import *


class Game:
    def __init__(self):
        pass

    def run_game(self):
        self.display_rules()
        self.display_welcome()
        self.play()
        self.display_winner()

    def display_rules(self):
        rules = ["Rules:", "scissors cuts paper", "paper covers rock", "rock crushes scissors", "lizard easts paper", "paper disproves spock", "spock vaporizes rock", "lizard poisons spock", "scissors decapitate lizard", "spock smashes scissors"]
        print(*rules, sep = "\n")

    def display_welcome(self):
        user_choice = ["Choose a mode:", "1: PvP", "2: PvE",  "3: Demo Mode"]
        print(*user_choice, sep = "\n")
        choice_input = input("Which mode do you choose? 1, 2 or 3:")
        if int(choice_input) == 1:
            print("Great, grab a partner and let's play!")
        elif int(choice_input) == 2:
            print("You think you can beat the AI?")
        elif int(choice_input) == 3:
            print("Watch and learn.")
        return choice_input

    def player_mode(self):
        if Game.display_welcome.choice_input == 1:
            player_one = input("Enter player 1 name:")
            player_two = input("Enter player 2 name:")
            return player_one and player_two
        elif Game.display_welcome.choice_input == 2:
            player_one = input("Enter player 1 name:")
            return player_one
        elif Game.display_welcome.choice_input == 3:
            


    def play(self):
        pass

    def display_winner(self):   
        pass

        

    