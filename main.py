from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

def game(lvl):
    # Screen Setup
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.colormode(255)

    # Turtle Setup
    player = Player()

    # Scoreboard Setup
    scoreboard = Scoreboard(lvl)

    # Car Manager Setup
    car_manager = CarManager(lvl)

    # Control listeners
    screen.listen()
    screen.onkeypress(fun=player.move_up, key="Up")
    screen.onkeypress(fun=player.move_down, key="Down")
    screen.onkeypress(fun=player.move_left, key="Left")
    screen.onkeypress(fun=player.move_right, key="Right")

    # Main Game Loop
    is_game = True
    while is_game:
        screen.update()
        time.sleep(0.1)
        car_manager.move_cars()

        if player.ycor() > 290:
            screen.clear()
            lvl += 2
            game(lvl)

        for car in car_manager.cars_list:
            if player.distance(car) < 30:
                scoreboard.game_over()
                is_game = False


    screen.exitonclick()

lvl = 5
game(lvl)