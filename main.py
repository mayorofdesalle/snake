from turtle import Screen
from snake import Snake
import time

# Set up screen
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
screen.listen()


# Start the game
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move('R')
    

screen.exitonclick()