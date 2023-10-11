from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")
snake = Snake(0, 0, 3)
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.2)
    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment) < 15:
            scoreboard.reset()
            snake.reset()
    snake.move()
    if snake.segment[0].distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase()
    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or \
            snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

screen.exitonclick()
