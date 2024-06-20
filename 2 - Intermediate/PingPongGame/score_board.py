from turtle import Turtle


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('grey')
        self.goto(x, y)
        self.score = 0

    def scores(self):
        self.score += 1

    def output(self):
        self.clear()
        self.pendown()
        self.write(f'{self.score}', False, 'center', ('Arial', 32, 'bold'))
        self.penup()