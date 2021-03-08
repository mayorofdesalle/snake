from playsound import playsound
from random import choice
from turtle import Screen
from snake import Snake
from food import Food
from ui import UI
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

# Menu
idle = True
def start():
    global idle
    idle = False

while idle:
    x = snake.head.xcor()
    y = snake.head.ycor()
    if (x, y) == (20, 20):
        snake.down()
    elif (x, y) == (20, -20):
        snake.left()
    elif (x, y) == (-20, -20):
        snake.up()
    elif (x, y) == (-20, 20):
        snake.right()
    snake.move()
    screen.onkeypress(start)
    time.sleep(0.1)
    screen.update()

food = Food()
UI = UI()
delay = 0.1
playsound(f'./res/sound/snake.wav', False)
while True:
    screen.update()
    time.sleep(delay)
    if snake.move():
        if snake.head.distance(food) < 10:
            playsound(f'./res/sound/food{(choice(range(1000))%5)+1}.wav', False)
            if UI.increase_score() and delay > 0.05:
                delay -= 0.005
            snake.grow()
            food.random(snake.get_pos())
    else:
        playsound(f'./res/sound/death.wav', False)
        screen.bgpic("res/death_screen.png")
        UI.game_over()
        time.sleep(2)
        UI.reset()
        snake.reset()
        playsound(f'./res/sound/snake.wav', False)
        screen.bgpic("res/screen.png")
        food.random(snake.get_pos())
        delay = 0.1