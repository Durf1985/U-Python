from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
speed = 0.1
while game_is_on:

    time.sleep(speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.paddler_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        if speed > 0.05:
            speed -= 0.03


    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        if speed > 0.05:
            speed -= 0.03

            
screen.exitonclick()
