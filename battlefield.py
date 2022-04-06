from human_player import Human_Player
from ai import Ai

class Battlefield():
    def __init__(self):
        self.player_1 = Human_Player
        self.player_2 = None
        self.opponent_choice = ""
        pass

    def display_welcome(self):
        print(" Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("""Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock,

Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock""")

    def choose_opponent(self):
        while self.opponent_choice != "Human" or "AI":
            print("Please choose an opponent")
            self.opponent_choice = input("Human, or AI?")
            if self.opponent_choice == "Human":
                self.player_2 = Human_Player
                break
            elif self.opponent_choice == "AI":
                self.player_2 = Ai
                break
            else:
                print("Invalid input. Please choose 'Human' or 'AI' ")
        print(f'Your opponent is now {self.opponent_choice}')

    def the_game(self):
        player_1_score = 0
        player_2_score = 0
        while (player_1_score < 2) and (player_2_score < 2):#JUST ADDED SELF. TO PLAYER CHOICE
            self.player_1_choice = self.player_1.choose_gesture(self)
            self.player_2_choice = self.player_2.choose_gesture(self)
            if  (player_1_choice == "Rock") and (player_2_choice == "Scissors" or "Lizard"):#Rock
                print(f"Rock beats{player_2_choice}.")
                print("Player 1 wins this round")
                player_1_score += 1
            elif (player_2_choice == "Rock") and (player_1_choice == "Scissors" or "Lizard"):
                print(f"Rock beats{player_1_choice}.")
                print("Player 2 wins this round")
                player_2_score += 1
            elif (player_1_choice == "Scissors") and (player_2_choice == "Paper" or "Lizard"):#Scissors
                print(f"Scissors beats {player_2_choice}.")
                print ("Player 1 wins this round")
                player_1_score += 1
            elif (player_2_choice == "Scissors") and (player_1_choice == "Paper" or "Lizard"):
                print(f"Scissors beats {player_1_choice}.")
                print("Player 2 wins this round")
                player_2_score += 1
            elif (player_1_choice == "Paper") and player_2_choice == "Spock" or "Rock":#Paper
                print(f"Paper beats {player_1_choice}.")
                print("Player 1 wins this round")
                player_1_score += 1
            elif (player_2_choice == "Paper") and (player_1_choice == "Spock" or "Rock"):
                print(f"Paper beats {player_1_choice}.")
                print("Player 2 wins this round")
            elif (player_1_choice == "Spock") and (player_2_choice == "Scissors" or "Rock"):#Spock
                print(f"Spock beats {player_2_choice}.")
                print("Player 1 wins this round")
                player_1_score += 1
            elif (player_2_choice == "Spock") and (player_1_choice == "Scissors" or "Rock"):
                print(f"Spock beats {player_1_choice}.")
                print("Player 2 wins this round")
            elif (player_1_choice == "Lizard") and (player_2_choice == "Paper" or "Spock"):#Lizard
                print(f"Lizard beats {player_2_choice}.")
                print("Player 1 wins this round")
            elif (player_2_choice == "Lizard") and (player_1_choice == "Paper" or "Spock"):#Lizard
                print(f"Lizard beats {player_1_choice}.")
                print("Player 2 wins this round")
            else:
                print("Tie! No points awarded!")