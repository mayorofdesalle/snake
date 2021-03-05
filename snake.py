from turtle import Turtle

class Snake:


    def __init__(self):
        self._body = []
        for i in range(3):
            self.extendBody(-i*10, 0)

    def extendBody(self, x, y):
        ''' Extends the body from the tail by one segment '''
        segment = Turtle('square')
        segment.shapesize(0.5, 0.5)
        segment.color(61, 80, 61)
        segment.pu()
        segment.goto(x, y)
        self._body.append(segment)

    def _pos_to_move(self, direction):
        ''' Calculates the coordinates to move according to the direction and checks boundaries '''
        current_x = self._body[0].xcor()
        current_y = self._body[0].ycor()
        x_dirs = {'R': 10, 'L': -10}
        y_dirs = {'U': 10, 'D': -10}
        current_x += x_dirs.get(direction, 0)
        current_y += y_dirs.get(direction, 0)
        boundaries = {180: -170, -180: 170}
        current_x = boundaries.get(current_x, current_x)
        current_y = boundaries.get(current_y, current_y)
        return (current_x, current_y)

    def move(self, direction):
        ''' Moves the head towards the direction, and all the rest into the position of the segment before them '''
        pos = self._pos_to_move(direction)
        if pos != self._body[1].pos():
            for i in range(len(self._body)-1, 0, -1):
                new_x = self._body[i - 1].xcor()
                new_y = self._body[i - 1].ycor()
                self._body[i].goto(new_x, new_y)
            self._body[0].goto(pos[0], pos[1])
            