from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.onkey(snake.turn_up, 'w')
    screen.onkey(snake.turn_left, 'a')
    screen.onkey(snake.turn_right, 'd')
    screen.onkey(snake.turn_down, 's')
    screen.listen()

    if -300 > snake.head.xcor() or snake.head.xcor() > 300 or -300 > snake.head.ycor() or snake.head.ycor() > 300 or snake.self_collision():
        print("Game Lost!")
        print(f"You scored {score_board.score}")
        break

    if snake.head.distance(food) < 15:
        snake.eat_food()
        score_board.scores()
        food.refresh()
        print('nom nom nom')

    score_board.output()
