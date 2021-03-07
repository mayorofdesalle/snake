from turtle import Turtle
HELL = (500, 500)


class Snake:


    def __init__(self):
        ''' Initializes the snake '''
        self._body = []
        self._create_snake()
        
    def _create_snake(self):
        ''' Creates the snake at the origin '''
        for i in range(3):
            self._extendBody(-i*10, 20)
        self._direction = 'R'
        self.head = self._body[0]

    def _extendBody(self, x, y):
        ''' Creates the body part for extension '''
        segment = Turtle('square')
        segment.shapesize(0.5, 0.5)
        segment.color(61, 80, 61)
        segment.pu()
        segment.goto(x, y)
        self._body.append(segment)

    def _pos_to_move(self):
        ''' Calculates the coordinates to move according to the direction and checks boundaries '''
        current_x = self.head.xcor()
        current_y = self.head.ycor()
        x_dirs = {'R': 10, 'L': -10}
        y_dirs = {'U': 10, 'D': -10}
        current_x += x_dirs.get(self._direction, 0)
        current_y += y_dirs.get(self._direction, 0)
        x_boundaries = {180: -170, -180: 170}
        y_boundaries = {140: -170, -180: 130}
        current_x = x_boundaries.get(current_x, current_x)
        current_y = y_boundaries.get(current_y, current_y)
        return (current_x, current_y)

    def move(self):
        ''' Moves the head towards the direction, and all the rest into the position of the segment before them '''
        pos = self._pos_to_move()
        if pos not in [s.pos() for s in self._body[1:]]:
            for i in range(len(self._body)-1, 0, -1):
                new_x = self._body[i - 1].xcor()
                new_y = self._body[i - 1].ycor()
                self._body[i].goto(new_x, new_y)
            self.head.goto(pos[0], pos[1])
            return True
        
        return False
    
    def right(self):
        ''' Sets the direction of the snake to the right '''
        if not self._direction == 'L':
            self._direction = 'R'

    def left(self):
        ''' Sets the direction of the snake to the left '''
        if not self._direction == 'R':
            self._direction = 'L'

    def up(self):
        ''' Sets the direction of the snake upwards '''
        if not self._direction == 'D':
            self._direction = 'U'

    def down(self):
        ''' Sets the direction of the snake downwards '''
        if not self._direction == 'U':
            self._direction = 'D'

    def grow(self):
        ''' Extends the snake's body by one segment '''
        self._extendBody(*self._body[-1].pos())

    def get_pos(self):
        ''' Returns the position of the snake's whole body '''
        return [p.pos() for p in self._body]

    def reset(self):
        ''' Recreates the snake at the origin '''
        for seg in self._body:
            seg.goto(HELL)
        self._body.clear()
        self._create_snake()