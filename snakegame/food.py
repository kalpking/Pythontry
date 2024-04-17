from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")

    def refresh(self):
        random_occur_x = random.randint(-260, 260)
        random_occur_y = random.randint(-260, 260)
        self.goto(random_occur_x, random_occur_y)
