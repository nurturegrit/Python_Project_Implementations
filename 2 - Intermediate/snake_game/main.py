from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.bgcolor('black')
screen.title("My Snake Game")
screen.setup(600,600)
screen.tracer(0)

positions = [(0,0),(-20,0),(-40,0)]
snake_body = []

for position in positions:
    new_segment = Turtle(shape='square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    snake_body.append(new_segment)

screen.update()
game_is_on = True
def right():
    snake_body[0].right(90)
def left():
    snake_body[0].left(90)
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for i in range(len(snake_body) -1,0, -1):
        new_x = snake_body[i-1].xcor()
        new_y = snake_body[i-1].ycor()
        snake_body[i].goto(new_x,new_y)

    snake_body[0].forward(20)
    x = snake_body[0].xcor()
    y = snake_body[0].ycor()
    if y <= -300 or x <= -300 or x >= 300 or y >= 300:
        game_is_on = False
    elif (x,y) in positions:
        game_is_on = False
    positions = [segment.pos() for segment in snake_body]
    screen.onkey(left,'a')
    screen.onkey(right, 'd')
    screen.listen()
screen.exitonclick()
