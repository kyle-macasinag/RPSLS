from human_player import Human_Player
from ai import Ai

class Battlefield():
    def __init__(self):
        self.player_1 = Human_Player
        self.player_2 = None
        self.opponent_choice = ""
        self.player_1_score = 0
        self.player_2_score = 0
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
        while (self.player_1_score < 2) and (self.player_2_score < 2):
            print(f"The current score is: {self.player_1_score} to {self.player_2_score}")
            self.player_1_choice = self.player_1.choose_gesture(self)
            self.player_2_choice = self.player_2.choose_gesture(self)
            if  (self.player_1_choice == "Rock") and ((self.player_2_choice == "Scissors") or (self.player_2_choice == "Lizard")):#Rock
                print(f"Rock beats {self.player_2_choice}.")
                print("Player 1 wins this round")
                self.player_1_score += 1
            elif (self.player_2_choice == "Rock") and ((self.player_1_choice == "Scissors") or (self.player_1_choice == "Lizard")):
                print(f"Rock beats {self.player_1_choice}.")
                print("Player 2 wins this round")
                self.player_2_score += 1
            elif (self.player_1_choice == "Scissors") and ((self.player_2_choice == "Paper") or (self.player_2_choice == "Lizard")):#Scissors
                print(f"Scissors beats {self.player_2_choice}.")
                print ("Player 1 wins this round")
                self.player_1_score += 1
            elif (self.player_2_choice == "Scissors") and ((self.player_1_choice == "Paper") or (self.player_1_choice == "Lizard")):
                print(f"Scissors beats {self.player_1_choice}.")
                print("Player 2 wins this round")
                self.player_2_score += 1
            elif (self.player_1_choice == "Paper") and ((self.player_2_choice == "Spock") or (self.player_2_choice == "Rock")):#Paper
                print(f"Paper beats {self.player_2_choice}.")
                print("Player 1 wins this round")
                self.player_1_score += 1
            elif (self.player_2_choice == "Paper") and ((self.player_1_choice == "Spock") or (self.player_1_choice == "Rock")):
                print(f"Paper beats {self.player_1_choice}.")
                print("Player 2 wins this round")
                self.player_2_score += 1
            elif (self.player_1_choice == "Spock") and ((self.player_2_choice == "Scissors") or (self.player_2_choice == "Rock")):#Spock
                print(f"Spock beats {self.player_2_choice}.")
                print("Player 1 wins this round")
                self.player_1_score += 1
            elif (self.player_2_choice == "Spock") and ((self.player_1_choice == "Scissors") or (self.player_1_choice == "Rock")):
                print(f"Spock beats {self.player_1_choice}.")
                print("Player 2 wins this round")
                self.player_2_score += 1
            elif (self.player_1_choice == "Lizard") and ((self.player_2_choice == "Paper") or (self.player_2_choice == "Spock")):#Lizard
                print(f"Lizard beats {self.player_2_choice}.")
                print("Player 1 wins this round")
                self.player_1_score += 1
            elif (self.player_2_choice == "Lizard") and ((self.player_1_choice == "Paper") or (self.player_1_choice == "Spock")):
                print(f"Lizard beats {self.player_1_choice}.")
                print("Player 2 wins this round")
                self.player_2_score += 1
            else:
                print("Tie! No points awarded!")
        if self.player_1_score == 2 or self.player_2_score == 2:
                    self.display_winner()    

        

    def display_winner(self):
        if self.player_1_score == 2:
            print(f"Player 1 wins! The final score is {self.player_1_score} to {self.player_2_score}")
        elif self.player_2_score == 2:
            print(f"Player 2 wins! The final score is {self.player_2_score} to {self.player_1_score}")

    def start_game(self):
        self.display_welcome()
        self.choose_opponent()
        self.the_game()
