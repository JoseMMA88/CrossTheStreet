from turtle import Turtle
from random import randint


class CarManager:

    def __init__(self, lvl):
        self.cars_list = []
        self.num_cars = lvl
        self.cars_speed = []

        for _ in range(self.num_cars):
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=2, stretch_len=1)
            car.setheading(90)
            color = (randint(0, 200), randint(0, 200), randint(0, 200))
            car.color(color)
            car.penup()
            car.goto(randint(-280, 280), randint(-220, 220))
            self.cars_list.append(car)

            if self.num_cars > 11:
                self.cars_speed.append(randint(-20, -10))
            else:
                self.cars_speed.append(-10)

    def move_cars(self):
        for i in range(len(self.cars_list)):
            if self.cars_list[i].xcor() < -300:
                self.cars_list[i].goto(300, randint(-220, 220))
            self.cars_list[i].goto(self.cars_list[i].xcor() + self.cars_speed[i], self.cars_list[i].ycor())

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
        for i in range(len(self.cars_list) - 1):
            self.cars_list[i].clear()