from racket import Racket
from turtle import Turtle, Screen
from ball import Ball
from score_board import Score
import time
import random

screen = Screen()
screen.bgcolor('black')
screen.title('Ping Pong Game')
screen.setup(1000,600)
screen.tracer(0)

racket1 = Racket()
racket1.goto(-450, 0)

racket2 = Racket()
racket2.goto(450, 0)

score1 = Score(-30, 250)
score2 = Score(30, 250)

score1.output()
score2.output()
game_is_on = True
ball = Ball()

def main():
    while game_is_on:
        ball.move()
        time.sleep(0.05)
        if ball.collision(racket1):
            ball.bounce(racket1)
        if ball.collision(racket2):
            ball.bounce(racket2)
        if ball.ycor() >= 290:
            ball.setheading(ball.heading() - random.randint(30, 55))
        if ball.ycor() <= -290:
            ball.setheading(ball.heading() + random.randint(30, 55))
        if ball.xcor() >= 500:
            score1.scores()
            score1.output()
            time.sleep(1)
            ball.goto(0, 0)
            return True
        if ball.xcor() <= -500:
            score2.scores()
            score2.output()
            time.sleep(1)
            ball.goto(0, 0)
            return True
        screen.update()
        screen.onkey(racket2.down, 'Down')
        screen.onkey(racket1.down, 's')
        screen.onkey(racket2.up, 'Up')
        screen.onkey(racket1.up, 'w')
        screen.update()
        screen.listen()

if __name__ == '__main__':
    while True:
        if main():
            choice = screen.textinput('Continue Playing?',"Type 'Y' to continue or 'N' to quit.").strip().lower()
        if choice == 'y':
            time.sleep(0.5)
            continue
        else:
            if score1.score > score2.score:
                print("Player 1 wins")
            elif score1.score < score2.score:
                print("Player 2 wins")
            elif score1.score > 10:
                print("It's a tie! You both played great!")
            else:
                print("It's a Tie!")
            break

screen.exitonclick()

