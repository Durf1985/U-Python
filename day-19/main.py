import turtle

t = turtle.Turtle()

screen = turtle.Screen()


def move_forward():
    t.forward(10)


def backward():
    t.back(10)


def clockwise():
    t.circle(10)


def counter_clockwise():
    t.circle(-100)


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(backward, "s")
screen.onkey(clockwise, )
screen.exitonclick()
