from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,280)
        self.color('green')
        self.update_highscore()

    def output(self):
        self.showturtle()
        self.clear()
        self.write(f'Score: {self.score} HighScore: {self.HIGHSCORE}',False,'center',('Arial', 15, 'bold'))
        self.hideturtle()

    def scores(self):
        self.score += 1

    def update_highscore(self):
        with open('highscore.txt', 'r+') as file:
            self.HIGHSCORE = file.read()
        if self.HIGHSCORE == "":
            self.HIGHSCORE = 0
        else:
            self.HIGHSCORE = int(self.HIGHSCORE)

    def reset(self):
        self.clear()
        self.score = 0
        self.update_highscore()
        self.output()