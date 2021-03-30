from turtle import Turtle
from random import choice
from numpy import arange


class Food(Turtle):


    def __init__(self, food_type='square'):
        ''' Render a piece of food on a random position in the screen'''
        super().__init__()
        self.shape(food_type)
        self.penup()
        self.speed('fastest')
        self._calculate_vals()
        self.shapesize(0.3, 0.3, 3)
        self.color((61, 80, 61), (187, 226, 205))
        eval('self.random()' if food_type=='square' else 'self.remove()')


    def _calculate_vals(self):
        ''' Calculate valid positions and headings '''
        x_vals = arange(-170, 170, 10)
        y_vals = arange(-170, 140, 10)
        self._vals = [(x, y) for x in x_vals for y in y_vals] 
        self._head_vals = arange(0, 360, 15)

    def random(self, exclude=[]):
        ''' Teleport the food to a random position and changes the heading'''
        self.showturtle()
        val = choice([p for p in self._vals if p not in exclude])
        self.goto(val)
        self.setheading(choice(self._head_vals))

    def remove(self):
        ''' Hide the food'''
        self.hideturtle()
