from turtle import Turtle, Screen


timmy = Turtle()


def move_forwards():
    timmy.forward(5)



def move_back():
    timmy.backward(5)


def turn_left():
    timmy.left(2)


def turn_right():
    timmy.right(2)


def draw_curve():
    for i in range(180):
        timmy.right(2)
        timmy.forward(5)
def etch_a_sketch():
    timmy.speed(3)
    screen = Screen()
    screen.onkeypress(fun=timmy.clear,key='c')
    screen.onkey(fun=move_back,key='s')
    screen.onkey(fun=move_forwards,key='w')
    screen.onkey(fun=turn_right,key='d')
    screen.onkey(fun=turn_left,key='a')
    screen.onkey(fun=draw_curve,key='o')
    screen.onkey(fun=timmy.home,key='h')
    screen.onkey(fun=timmy.penup,key='u')
    screen.onkey(fun=timmy.pendown,key='p')
    screen.listen()

    screen.exitonclick()

etch_a_sketch()