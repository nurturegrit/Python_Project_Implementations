from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,280)
        self.color('green')

    def output(self):
        self.showturtle()
        self.clear()
        self.write(f'Score: {self.score}',False,'center',('Arial', 15, 'bold'))
        self.hideturtle()

    def scores(self):
        self.score += 1

