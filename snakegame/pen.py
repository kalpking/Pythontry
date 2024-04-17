from turtle import Turtle


class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.setpos(x=-20, y=260)

    def increased_score(self):
        self.score += 1
        self.clear()
        self.pendown()
        self.write(f"Score: {self.score} ", align="center", font=("areal", 24, "normal"))


