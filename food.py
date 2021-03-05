from turtle import Turtle
from random import choice
from numpy import arange


class Food(Turtle):


    def __init__(self):
        ''' Creates a piece of food on a random position in the screen'''
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(0.3, 0.3, 3)
        self.color((61, 80, 61), (187, 226, 205))
        self.speed('fastest')
        self._pos_x_vals = arange(-170, 170, 10)
        self._pos_y_vals = arange(-170, 140, 10)
        self._head_vals = arange(0, 360, 15)
        self.random()
    
    def random(self):
        ''' Teleports the food to a random position and changes the heading'''
        self.goto(choice(self._pos_x_vals), choice(self._pos_y_vals))
        self.setheading(choice(self._head_vals))