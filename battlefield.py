class Battlefield():
    def __init__(self, choice):
        self.choice = choice
       
    pass

    def display_welcome(self):
        print(" Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("""Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock,

Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock""")

    def choose_opponent(self):
        while self.choice != "Human" or "AI":
            print("Please choose an opponent")
            self.choice = input("Human, or AI?")
            if self.choice == "Human":
                 break
            elif self.choice == "AI":
                break
            else:
                print("Please choose 'Human' or 'AI' ")