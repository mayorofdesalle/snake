from turtle import Turtle
from random import choice
import time
HELL = (500, 500)
GAME_OVER_WORDS = ['GAME OVER', 'MEH', 'TRY AGAIN', 
                    'THAT YOUR BEST?', 'OUROBOROS MUCH?', 
                    'NAH', 'THAT HUNGRY?', 'GO VEGETERIAN',
                    'HELL AND BACK', 'BON APPETIT']


class UI(Turtle):


    def __init__(self):
        ''' Creates the scoreboard '''
        super().__init__()
        # Scoreboard
        self._score = 0
        self.hideturtle()
        self.pu()
        self._update_scoreboard()

    def _update_scoreboard(self):
        ''' Updates the scoreboard '''
        self.clear()
        self.goto(-170, 145)
        self.color(61, 80, 61)
        self.write(str(self._score).zfill(4), align='left', font=('Digital-7', 20, 'bold'))

    def increase_score(self):
        ''' Increases the score by 1 '''
        self._score += 1
        self._update_scoreboard()
        if self._score%10 == 0:
            return True
        return False

    def game_over(self):
        ''' Shows the game over screen '''
        self.goto(170, 145)
        self.write(choice(GAME_OVER_WORDS), align='right', font=('Digital-7', 20, 'bold'))

    def reset(self):
        # Clear the screen
        self.goto(HELL)
        self.clear()
        # Reset the score
        self._score=0
        self._update_scoreboard()