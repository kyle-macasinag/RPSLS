class Players():
    def __init__(self):
        self.points = 0
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']
        self.chosen_gesture = ''

    def choose_gesture(self):
        self.chosen_gesture = input(f'Please choose a gesture: {self.gestures}')

    