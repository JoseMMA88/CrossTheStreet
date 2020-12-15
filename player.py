from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)
        self.move_speed = 10
        self.setheading(90)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.move_speed)

    def move_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - self.move_speed)

    def move_left(self):
        if self.xcor() > -280:
            self.goto(self.xcor() - self.move_speed, self.ycor())

    def move_right(self):
        if self.xcor() < 280:
            self.goto(self.xcor() + self.move_speed, self.ycor())

    def reset_pos(self):
        self.goto(0, -280)
