from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, x, y, segment_count, snake_speed=20):
        self.segment = []
        self.speed = snake_speed
        self.create_segment(x, y, segment_count)

    def create_segment(self, x, y, count):
        for turtle in range(0, count):
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.setpos(x, y)
            x -= 20
            self.segment.append(t)
        print(self.segment)

    def reset(self):
        for i in self.segment:
            i.goto(1000, 1000)
        self.segment.clear()
        self.create_segment(0, 0, 3)

    def extend(self):
        x = self.segment[-1].xcor()
        y = self.segment[-1].ycor()
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setpos(x, y)
        self.segment.append(new_segment)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            x = self.segment[seg - 1].xcor()
            y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x, y)
        self.segment[0].forward(self.speed)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].seth(90)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].seth(270)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].seth(180)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].seth(0)
