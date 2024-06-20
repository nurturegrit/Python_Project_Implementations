from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('red')
        self.penup()
        self.hideturtle()
        self.goto(150, 250)

    def scores(self):
        self.score += 1

    def output(self):
        self.write(f'Score:{self.score}', False, 'left', FONT)