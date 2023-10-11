import random
import turtle

import colorgram
import turtle as t

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")

screen = t.Screen()


def next_line():
    y = timmy.ycor()
    timmy.setpos(0, y + 50)


def painting_dot(colors):
    x = int(timmy.xcor())
    y = int(timmy.ycor())
    timmy.speed(1)

    for i in range(11):
        timmy.dot(10, random.choice(colors))
        timmy.setpos(x, y)
        x += 50



color = []
cologr = colorgram.extract("img.jpg", 10)
for i in cologr:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    color.append(new_color)

turtle.colormode(255)
timmy.penup()
for i in range(11):
    painting_dot(color)

    next_line()

# screen.exitonclick()
