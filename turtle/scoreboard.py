from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(-280, 260)
        self.draw_score()

    def increase_score(self):
        self.score += 1
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)
