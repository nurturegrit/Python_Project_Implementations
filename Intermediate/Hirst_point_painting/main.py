import colorgram
from turtle import Turtle, Screen
import random


Colors = colorgram.extract('./DHS4591_771_0.jpg', 40)
def make_painting(length, l_dots, height, h_dots, thick):
    """The functions takes all inputs of int, length and height are the dimensions of the area painted on screen.
    The l_dots are dots that made in length and h_dots are dots that are made in height.
    thick is size of the dots
    All dots are in random sequence from a list of colors"""
    n = int(length/l_dots)
    m = int(height/h_dots)
    timmy = Turtle()
    timmy.speed(0)
    x, y = timmy.pos()
    timmy.hideturtle()
    for h in range(h_dots):
        x, y = timmy.pos()
        for l in range(l_dots):
            timmy.pendown()
            r, g, b = random.choice(Colors).rgb
            timmy.pencolor(r/255, g/255, b/255)
            timmy.dot(thick)
            timmy.penup()
            timmy.forward(n)
        timmy.penup()
        timmy.goto(x,y+m)
        timmy.pendown()


make_painting(200, 15,100,10,5)

screen = Screen()
screen.exitonclick()
