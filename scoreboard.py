from turtle import Turtle


FONT = ("Verdana", 20, "normal")
GAME_OVER_FONT = ("Verdana", 46, "normal")


class Scoreboard(Turtle):

    def __init__(self, lvl):
        super().__init__()
        self.lvl = lvl
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.rewrite()

    def rewrite(self):
        self.clear()
        self.write(arg=f"Level: {self.lvl}", font=FONT)

    def update_lvl(self):
        self.lvl += 1
        self.rewrite()

    def game_over(self):
        self.goto(-200, 0)
        self.write(arg="GAME OVER", font=GAME_OVER_FONT)
