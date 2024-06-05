import tkinter

def button_clicked():
    user_input = input_field.get()
    if user_input:
        my_label.config(text=f"{user_input}")
    else:
        my_label.config(text="I Got Clicked")
# Makes a window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=200, height=300)

# Makes a Label
my_label = tkinter.Label(font=("Arial", 24, "bold"), text="I am a Label")
# Places the Label on the screen
my_label.pack(expand=True)
# .pack(side="left/top/bottom/right" , expand= Boolean_Value) --side changes the position of the label
# --expand will 'try' to take the entire screen of the window

# Entry --Input Field
input_field = tkinter.Entry(width=10)
input_field.pack()

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Keeps the window on screen and listens to the actions of the user
window.mainloop()