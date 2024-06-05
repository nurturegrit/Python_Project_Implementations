from tkinter import *

def m2k():
    m = float(n_input.get())
    k = m * 1.609
    output["text"] = f"{int(k) if k.is_integer() else f'{k:.2f}'}"

window = Tk()
window.title("Miles to KiloMeter")
window.minsize(width=400, height=250)
window.grid()

n_input = Entry(width=15)
n_input.place(x=150, y=35)

miles = Label(text="Miles", font=("Ariel", 16, "normal"))
miles.place(x=300, y=30)

equal = Label(text="Equals To", font=("Ariel", 14, "normal"))
equal.place(x=30, y=60)

output = Label(text="0", font=("Ariel", 16, "normal"))
output.place(x=180, y=60)

kilometer = Label(text="KiloMeter", font=("Ariel", 16, "normal"))
kilometer.place(x=300, y=60)

button = Button(text="Covert", command=m2k, font=("Ariel", 14, "normal"))
button.place(x=150, y=90)
window.mainloop()