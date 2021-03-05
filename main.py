from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=450, height=450)
screen.screensize(350, 350)
screen.bgpic("res/screen.png")
screen.colormode(255)
screen.bgcolor(62, 70, 89)
screen.tracer(0)
screen.title('Snake')

# Initialize the game
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Set up keys and start listening
screen.listen()
screen.onkey(snake.right, 'Right')
screen.onkey(snake.right, 'd')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.left, 'a')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.down, 's')

# Start the game
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.07)
    if snake.move():
        if snake.head.distance(food) < 10:
            scoreboard.increase()
            snake.grow()
            food.random()
    else:
        game_over = True
        scoreboard.game_over()

screen.exitonclick()