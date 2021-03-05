from turtle import Turtle
import time


class Scoreboard(Turtle):


    def __init__(self):
        ''' Creates the scoreboard '''
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(61, 80, 61)
        self.pu()
        self.goto(-170, 145)
        self.write(str(self.score).zfill(4), align='left', font=('Digital-7', 20, 'bold'))

    def _update_scoreboard(self):
        ''' Updates the scoreboard '''
        self.clear()
        self.write(str(self.score).zfill(4), align='left', font=('Digital-7', 20, 'bold'))

    def increase(self):
        ''' Increases the score by 1 '''
        self.score += 1
        self._update_scoreboard()

    def game_over(self):
        ''' Shows the game over screen '''
        over = Turtle()
        over.hideturtle()
        over.color(61, 80, 61)
        over.pu()
        over.write("GAME OVER", align='center', font=('Digital-7', 20, 'bold'))