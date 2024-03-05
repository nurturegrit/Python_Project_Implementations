from turtle import Turtle


class Racket(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=0.5)

    def up(self):
        x, y = self.pos()
        if y + 20 > 300:
            return
        self.goto(x, y+20)

    def down(self):
        x, y = self.pos()
        if y - 20 < -300:
            return
        self.goto(x, y - 20)
