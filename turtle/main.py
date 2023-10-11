import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager(15)
car_manager.start_position()

screen.onkeypress(turtle.move, "w")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    if turtle.ycor() == 300:
        turtle.next_round()
        scoreboard.increase_score()
    for car in car_manager.cars:
        if turtle.distance(car) < 22:
            print("Game Over")
            game_is_on = False

screen.exitonclick()
