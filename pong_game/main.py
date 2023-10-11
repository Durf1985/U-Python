from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    print("Ball position:", ball.xcor(), ball.ycor())
    print("Right paddle position:", r_paddle.xcor(), r_paddle.ycor())
    print("Distance to right paddle:", ball.distance(r_paddle))
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        # print("Make")
        ball.paddler_bounce()

    if ball.xcor() > 400 or ball.xcor() < -400:
        print("Game Over")
        break

screen.exitonclick()
