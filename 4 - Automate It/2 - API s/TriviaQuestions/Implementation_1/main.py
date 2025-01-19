from tkinter import *
import requests
import time
ANSWER = None
SCORE = 0
N = 1


# --------------------------- Answer Commands --------------------------- #
def tick_clicked():
    global SCORE, ANSWER
    if ANSWER:
        SCORE += 1
        canvas.config(bg="green")
    else:
        canvas.config(bg="red")
    score_label.config(text=f"Score:{SCORE}")
    window.update()
    time.sleep(0.2)
    canvas.config(bg="white")
    put_question()


def cross_clicked():
    global SCORE, ANSWER
    if not ANSWER:
        SCORE += 1
        canvas.config(bg="green")
    else:
        canvas.config(bg="red")
    score_label.config(text=f"Score:{SCORE}")
    window.update()
    time.sleep(0.2)
    canvas.config(bg="white")
    canvas.config(bg="white")
    put_question()
# ---------------------------- Get Question from API -------------------- #


def put_question():
    global ANSWER, N
    question, ANSWER = get_question()
    canvas.itemconfig(text, text=question)
    N += 1


def get_question():
    response = requests.get(url="https://opentdb.com/api.php?amount=1&category=9&difficulty=medium&type=boolean")
    response.raise_for_status()
    return response.json()["results"][0]["question"].replace("&quot;", "\""), response.json()["results"][0]["correct_answer"]
# ---------------------------------- User UI ---------------------------- #

question, ANSWER = get_question()

window = Tk()
window.config(height=600, width=400, bg="#375362", pady=30, padx=15)
window.grid()

score_label = Label(text=f"Score:{SCORE}")
score_label.grid(row=0, column=1)
canvas = Canvas(height=300, width=300, bg="white")
canvas.grid(row=1, column=0, columnspan=2, pady=30, padx=15)
text = canvas.create_text(75, 100, text=f"{question}", font=("Arial", 15, "italic"))

tick = PhotoImage(file="images/true.png")
cross = PhotoImage(file="images/false.png")

tick_button = Button(image=tick, command=tick_clicked)
cross_button = Button(image=cross, command=cross_clicked)

tick_button.grid(row=2, column=0)
cross_button.grid(row=2, column=1)
window.mainloop()
print(f"Your Final Score was {SCORE}/{N}")

