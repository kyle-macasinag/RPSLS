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
