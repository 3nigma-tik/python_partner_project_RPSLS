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
        # self.play()
        # self.display_winner()


    def display_rules(self):
        rules = ["Rules:", "scissors cuts paper", "paper covers rock", "rock crushes scissors", "lizard easts paper", "paper disproves spock", "spock vaporizes rock", "lizard poisons spock", "scissors decapitate lizard", "spock smashes scissors"]
        print(*rules, sep = "\n")


    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!")        
        user_choice = ["Choose a mode:", "1: PvP", "2: PvE",  "3: Demo Mode"]
        print(*user_choice, sep = "\n")      
        
        while True:                
            choice_input = int(input("Which mode do you choose? 1, 2 or 3:"))                             

            if int(choice_input) == 1:
                print("Great, grab a partner and let's play!")
                self.mode = 1
                self.play()
            elif int(choice_input) == 2:
                print("You think you can beat the AI?")
                self.mode = 2
                self.play()
            elif int(choice_input) == 3:
                print("Watch and learn.")
                self.mode = 3 
                self.play()
                break
            else:
                print("try again.")
        
        

    #     return choice_input

    # def player_mode(self):
    #     if Game.display_welcome.choice_input == 1:
    #         player_one = input("Enter player 1 name:")
    #         player_two = input("Enter player 2 name:")
    #         return player_one and player_two
    #     elif Game.display_welcome.choice_input == 2:
    #         player_one = input("Enter player 1 name:")
    #         return player_one
    #     elif Game.display_welcome.choice_input == 3:
            



    def play(self):
        if self.mode == 1 or self.mode == 2:
            # Human
            player_one = Human('Player 1')
               
        elif self.mode == 3:
            # Demo
            player_one = AI('Deeper Blue')
               
            
        # Player 2
        if self.mode == 1:
            # Human
            player_two = Human('Player 2')
                
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
                print(f"Player 1 has {player_one.score} point/s")
            elif player_one_gesture in p_t_defeats:
                player_two.increase_score()
                print(f"Player 2 has {player_two.score} point/s")
                
            if player_one.score >= 2:
                self.winner = player_one
                self.display_winner()
            elif player_two.score >= 2:
                self.winner = player_two
                self.display_winner()




    def display_winner(self):   
        print(f"{self.winner.name} wins!!!")    