from player import Player
import random

class Ai(Player):
    def __init__():
        return super().__init__()

    def choose_gesture(self):
        self.ai_chosen = random.choice(self.gestures)
        print(f"AI has chosen {self.ai_chosen}")
        return self.ai_chosen