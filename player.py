class Player():
    def __init__(self):
        self.score = 0
        self.chosen_gesture = ''
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']

    def choose_gesture(self):


        self.chosen_gesture = input(f'Please choose a gesture: {self.gestures}')
        while self.chosen_gesture not in (self.gestures):
            print('Invalid input; please try again.')
            self.chosen_gesture = input(f'Please choose a gesture: {self.gestures}')
        return self.chosen_gesture
