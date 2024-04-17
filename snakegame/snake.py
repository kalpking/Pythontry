from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for new_turtle in STARTING_POSITION:
            self.add_segment(new_turtle)

    def add_segment(self, new_turtle):
        turs = Turtle()
        turs.penup()
        turs.shape("square")
        turs.goto(new_turtle)
        turs.color("white")
        self.segments.append(turs)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        for positions in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[positions - 1].xcor()
            new_ycor = self.segments[positions - 1].ycor()
            self.segments[positions].goto(new_xcor, new_ycor)
        self.segments[0].forward(20)

    def turn_right(self):
        self.segments[0].right(90)

    def turn_left(self):
        self.segments[0].left(90)
