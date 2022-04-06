class Players():
    def __init__(self, score, chosen_gesture):
        self.points = score
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']
        self.chosen_gesture = chosen_gesture

    def choose_gesture(self):
        print(f'Please choose a gesture: {self.gestures}')
        