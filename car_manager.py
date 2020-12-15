from turtle import Turtle
from random import randint


class CarManager:

    def __init__(self, lvl):
        self.cars_list = []
        self.num_cars = lvl
        self.cars_speed = -10

        for _ in range(self.num_cars):
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1.5, stretch_len=2)
            color = (randint(0, 200), randint(0, 200), randint(0, 200))
            car.color(color)
            car.penup()
            car.goto(randint(-280, 280), randint(-220, 220))
            self.cars_list.append(car)

    def move_cars(self):
        for car in self.cars_list:
            if car.xcor() < -300:
                car.goto(300, randint(-220, 220))
            car.goto(car.xcor() + self.cars_speed, car.ycor())

    def reset_cars(self):
        self.clear_cars()
        self.cars_list = []

        for _ in range(self.num_cars):
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1.5, stretch_len=2)
            color = (randint(0, 200), randint(0, 200), randint(0, 200))
            car.color(color)
            car.penup()
            car.goto(randint(-280, 280), randint(-220, 220))
            self.cars_list.append(car)

    def clear_cars(self):
        for car in self.cars_list:
            car.clear()