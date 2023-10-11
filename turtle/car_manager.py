from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_WIDTH = 25
SCREEN_HEIGHT = 500
MIN_Y = round(-SCREEN_HEIGHT / 2 + CAR_WIDTH)
MAX_Y = round(SCREEN_HEIGHT / 2 + CAR_WIDTH)
LANES = list(range(MIN_Y, MAX_Y, CAR_WIDTH))


class CarManager:
    def __init__(self, counter):
        self.counter = counter
        self.cars = []

    def start_position(self):
        random.shuffle(LANES)
        lanes_copy = LANES.copy()
        for i in range(self.counter):
            if not lanes_copy:
                lanes_copy = LANES.copy()
                random.shuffle(lanes_copy)
            lane = lanes_copy.pop()
            car = self.create()
            car.goto(250, lane)
            car.setheading(180)
            self.cars.append(car)

    @staticmethod
    def create():
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(1, 3)
        new_car.setheading(180)
        return new_car

    def move(self):
        for i in self.cars:
            speed = random.randint(5, 50)

            if i.xcor() < -300:
                i.goto(250,i.ycor())


            i.forward(speed + MOVE_INCREMENT)
