import turtle
import pandas as pd

# Initializing Screen
screen = turtle.Screen()
screen.title("U. S. States Game")
screen.bgpic("blank_states_img.gif")

# initializing Turtle
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()


def main():
    data = pd.read_csv("50_states.csv")
    states = data["state"].tolist()
    guessed_times = 0
    guessed = []
    score = 0
    while guessed_times <= 50:
        guess = screen.textinput(f"{guessed_times}/50", "Guess a State")
        if guess is None or guess in guessed:
            continue
        guess = guess.title()
        if guess == 'Exit':
            break
        guessed_times += 1
        if guess in states:
            score += 1
            found = data[data['state'] == guess]
            x, y = int(found['x'].iloc[0]), int(found['y'].iloc[0])
            writer.goto(x, y)
            writer.write(guess)
            guessed.append(guess)
    missed = []
    for state in states:
        if state not in guessed:
            missed.append(state)
    pd.Series(missed).to_csv("Missed_States.csv")
    return score


if __name__ == "__main__":
    score = main()
    print("You scored", score)


