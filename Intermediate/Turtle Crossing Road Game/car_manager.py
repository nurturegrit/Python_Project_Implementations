from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.color_list = COLORS
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_list = []

    def initialize_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle()
            new_car.penup()
            y = random.randint(-250, 250)
            new_car.goto(300, y)
            new_car.color(random.choice(self.color_list))
            new_car.shape('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.car_speed)
            if car.xcor() <= -300:
                self.car_list.remove(car)

    def speedup(self):
        self.car_speed += MOVE_INCREMENT


