from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.goto(position)

    def go_up(self):
        y = self.ycor()
        self.goto(self.xcor(), y + 40)

    def go_down(self):
        y = self.ycor()
        self.goto(self.xcor(), y - 40)