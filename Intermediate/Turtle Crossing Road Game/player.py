from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.penup()
        self.speed(0)
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() >= 280:
            self.goto(STARTING_POSITION)
            return True

    def collision(self, li):
        for car in li:
            if self.distance(car.pos()) <= 20:
                return True
        return False