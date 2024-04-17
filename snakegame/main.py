from turtle import Screen
import time
from snake import Snake
from food import Food
from pen import Pen

screen = Screen()
screen.listen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
pen1 = Pen()
game_is_on = True

point = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if screen.onkey(key="d", fun=snake.turn_right):
        snake.turn_right()
    elif screen.onkey(key="a", fun=snake.turn_left):
        snake.turn_left()

    if snake.segments[0].xcor() > 280 or snake.segments[0].ycor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        print("GAME OVER")

    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            game_is_on = False
            print("Game over")

    if snake.segments[0].distance(food) < 15:
        pen1.increased_score()
        food.refresh()
        snake.extend()

screen.exitonclick()
