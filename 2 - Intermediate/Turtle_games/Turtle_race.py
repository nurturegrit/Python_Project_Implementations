from turtle import Turtle, Screen
import random

def main():
    player_names = ['red', 'yellow', 'green', 'blue', 'purple', 'black']
    players = {}
    for player in player_names:
        p1 = player
        player = Turtle(shape='turtle')
        player.color(p1)
        player.penup()
        players[player] = p1
    screen = Screen()
    width = 500
    height = 400
    screen.setup(width,height)
    for n,player in enumerate(players.keys()):
        player.goto(x= -230, y= -180 + n*(height/len(players)))
    bet = screen.textinput(title='Which turtle will win the race?',prompt='Bet on : red/yellow/blue/black/green/purple').lower()
    finish = False
    while not finish:
        for player in players.keys():
            move = random.randint(5, 10)
            player.forward(move)
            x, y = player.pos()
            if x >= width//2:
                winner = player
                finish = True
                break
    if bet == players[winner]:
        print("You won!")
    else:
        print('You Lose')
    print(f"Winner is {players[winner].title()} Turtle!!")

    screen.exitonclick()
main()