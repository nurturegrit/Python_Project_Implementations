from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.speed(8)

    def move(self):
        self.forward(10)

    def collision(self, obj1):
        x_distance = abs(self.xcor() - obj1.xcor())
        y_distance = abs(self.ycor() - obj1.ycor())
        if x_distance < 20 and y_distance < 60:
            return True
        return False

    def bounce(self, obj):
        ball_angle = self.heading()
        obj_angle = obj.heading()
        diff_angle = ball_angle - obj_angle
        reflection_angle = 180 - ball_angle + 2*diff_angle*2
        y_distance = abs(self.ycor() - obj.ycor())
        if obj.xcor() > 0:
            self.setheading(reflection_angle - y_distance)
        else:
            self.setheading(reflection_angle + y_distance)