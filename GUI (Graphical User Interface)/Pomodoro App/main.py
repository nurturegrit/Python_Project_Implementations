from tkinter import *
import pygame
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
COUNTDOWN_TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_clicked():
    global REPS, COUNTDOWN_TIMER
    REPS = 0
    window.after_cancel(COUNTDOWN_TIMER)
    text.config(text="Timer")
    canvas.itemconfig(time, text="00:00")
    checkmark.config(text="")
    start.config(state=NORMAL)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_clicked():
    start.config(state=DISABLED)
    global REPS
    REPS += 1
    checkmark.config(text="✔" * (REPS // 2))
    if REPS == 8:
        text.config(text="BREAK", fg=RED)
        countdown(LONG_BREAK_MIN*60)
    elif REPS % 2 == 0:
        text.config(text="BREAK", fg=PINK)
        countdown(SHORT_BREAK_MIN*60)
    else:
        text.config(text="WORK", fg=GREEN)
        countdown(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_mins = count//60
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(time, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global COUNTDOWN_TIMER
        COUNTDOWN_TIMER = window.after(1000, countdown, count - 1)
    else:
        pygame.mixer.init()
        pygame.mixer.Sound(file="alarm-clock-short-6402.mp3").play()
        start_clicked()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text = Label(text="Timer", font=(FONT_NAME, 30, "normal"), bg=YELLOW, fg=GREEN)
text.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
time = canvas.create_text(100, 130, font=(FONT_NAME, 30, "bold"), fill="white", text="00:00")
canvas.grid(row=1, column=1)

start = Button(text="Start", highlightthickness=0, command=start_clicked)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_clicked)
reset.grid(row=2, column=2)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)
window.mainloop()