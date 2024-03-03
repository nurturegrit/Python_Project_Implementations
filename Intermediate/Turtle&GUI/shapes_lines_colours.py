from turtle import Turtle, Screen
import random


def draw_square(x: int):
    timmy = Turtle()
    for _ in range(4):
        timmy.forward(x)
        timmy.right(90.0)


def dotted_line(segiment_length: int, gap: int, times: int):
    timmy = Turtle()
    for i in range(times):
        timmy.penup()
        timmy.forward(segiment_length)
        timmy.pendown()
        timmy.forward(gap)


def random_color():
    r = random.random()
    b = random.random()
    g = random.random()
    return (r, g, b)


def random_walk(steps, length):
    angles = [0, 90, 180, 270]
    timmy = Turtle()
    timmy.pensize(3)
    timmy.speed(10)
    for _ in range(steps):
        timmy.color(random_color())
        timmy.setheading(random.choice(angles))
        timmy.forward(length)

# random_walk(1000, 30)


def draw_shapes(sides, size, colour='r'):
    r = -1
    if colour == 'r':
        r = random.random()
        b = random.random()
        g = random.random()
    if 360%sides != 0:
        return
    angle = 360/sides
    timmy = Turtle()
    if r == -1:
        timmy.pencolor(colour)
    else:
        timmy.pencolor((r, g, b))

    for _ in range(sides):
        timmy.right(angle)
        timmy.forward(size)


# for i in range(3,11):
#     draw_shapes(i, 100)

# def circles(number, radius):
#     remainder_angle = 360%number
#     angle = (360-remainder_angle)/number
#     residue_angle = remainder_angle/number
#     timmy = Turtle()
#     timmy.speed(0)
#     for _ in range(number):
#         timmy.circle(radius=radius)
#         timmy.color(random_color())
#         timmy.right(angle+residue_angle)

def circles(number, radius):
    """performed better than my adjustment earlier"""
    angle = 360/number
    timmy = Turtle()
    timmy.speed(0)
    for _ in range(number):
        timmy.circle(radius=radius)
        timmy.color(random_color())
        timmy.right(angle)

circles(50,100)





# dotted_line(10,10,10)

display = Screen()
display.exitonclick()