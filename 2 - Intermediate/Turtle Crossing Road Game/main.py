import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
cars = CarManager()


def main():
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        scoreboard.output()
        cars.initialize_car()
        screen.listen()
        screen.onkey(player.move,'w')
        if player.finish():
            scoreboard.scores()
            cars.speedup()
            scoreboard.clear()
        if player.collision(cars.car_list):
            return
        cars.move_cars()
        screen.update()

if __name__ == '__main__':
    while True:
        main()
        choice = screen.textinput(f'You Scored {scoreboard.score}','Do you want to play again?')
        if choice == 'y':
            continue
        else:
            break



