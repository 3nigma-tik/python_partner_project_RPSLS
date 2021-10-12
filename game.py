from gestures import Gestures
from players import Player
from human import Human
from ai import AI 
import random
from tkinter import *


class Game:
    def __init__(self):
        self.winner = False
        self.mode = 0

    def run_game(self):
        self.display_rules()
        self.display_welcome()
        self.play()
        self.display_winner()

    def display_welcome(self):
        user_choice = ["Choose a mode:", "1: PvP", "2: PvE",  "3: Demo Mode"]
        print(user_choice)
        choice_input = input("Which mode do you choose? 1, 2 or 3:")
        if int(choice_input) == 1:
            print("Great, grab a partner and let's play!")
            self.mode = 1
        elif int(choice_input) == 2:
            print("You think you can beat the AI?")
            self.mode = 2
        elif int(choice_input) == 3:
            print("Watch and learn.")
            self.mode = 3 
        

    def display_rules(self):
        rules = ["Rules:", "scissors cuts paper", "paper covers rock", "rock crushes scissors", "lizard easts paper", "paper disproves spock", "spock vaporizes rock", "lizard poisons spock", "scissors decapitate lizard", "spock smashes scissors"]
        print(*rules, sep = "\n")

    def play(self):
        if self.mode == 1 or self.mode == 2:
            # Human
            player_one = Human('Mr. Robot')
               
        elif self.mode == 3:
            # Demo
            player_one = AI('Deeper Blue')
               
            
        # Player 2
        if self.mode == 1:
            # Human
            player_two = Human('Bender')
                
        elif self.mode == 2 or self.mode == 3:
            # AI/Demo
            player_two = AI('Deep Blue')
                
        while not self.winner:
            # Player 1
            if self.mode == 1 or self.mode == 2:
                # Human
                
                player_one_gesture = player_one.pick_gesture()
                p_o_gestures = Gestures(player_one_gesture)
                p_o_defeats = p_o_gestures.defeats
            elif self.mode == 3:
                # Demo
                
                player_one_gesture = player_one.pick_gesture()
                p_o_gestures = Gestures(player_one_gesture)
                p_o_defeats = p_o_gestures.defeats
            
            # Player 2
            if self.mode == 1:
                # Human
                
                player_two_gesture = player_two.pick_gesture()
                p_t_gestures = Gestures(player_two_gesture)
                p_t_defeats = p_t_gestures.defeats
            elif self.mode == 2 or self.mode == 3:
                # AI/Demo
                
                player_two_gesture = player_two.pick_gesture()
                p_t_gestures = Gestures(player_two_gesture)
                p_t_defeats = p_t_gestures.defeats

            # did a player win
            if player_two_gesture in p_o_defeats:
                player_one.increase_score()
                print(player_one.score)
            elif player_one_gesture in p_t_defeats:
                player_two.increase_score()
                
            if player_one.score >= 2:
                self.winner = player_one
            elif player_two.score >= 2:
                self.winner = player_two




    def display_winner(self):   
        print(f"{self.winner.name} wins!!!")

        

    