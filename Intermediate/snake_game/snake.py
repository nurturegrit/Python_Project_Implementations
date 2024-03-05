from turtle import Turtle


class Snake:
    def __init__(self, positions=((0, 0), (-20, 0), (-40, 0)), m=20):
        self.starting_positions = positions
        self.body = []
        self.create_snake()
        self.move_distance = m
        self.head = self.body[0]

    def wall_collision(self):
        x, y = self.head.pos()
        if -300 <= x <= 300 and -300 <= y <= 300:
            return False
        return True

    def self_collision(self):
        for segment in self.body[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def create_snake(self):
        for position in self.starting_positions:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.body.append(new_segment)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.head.forward(self.move_distance)

    def eat_food(self):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.body[-1].pos())
        self.body.append(new_segment)

    def turn_right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)

    def turn_left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    def turn_up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)
