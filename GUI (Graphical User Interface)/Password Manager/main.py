from tkinter import *
from tkinter import messagebox
import random, string
import pyperclip
import json


# ----------------------------- PASSWORD SEARCH ----------------------------------- #
def search():
    website = www.get()
    email = username_entry.get()
    if not website:
        messagebox.showerror("No Website Name Provided!", message="Please Input A Website Name")
    elif not email:
        messagebox.showerror("No Email/Username Name Provided!", message="Please Input An Email or Username")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
            if data[website]["Email"] == email:
                password_entry.insert(0, data[website]["Password"])
        except FileNotFoundError:
            messagebox.showinfo(title="No Previous Records",
                                message="There are no previous entries saved in the database.")
            return
        except KeyError:
            messagebox.showinfo(title="Password Not Found", message="There are no relevant password entry for "
                                                                    f"\nEmail: {email}\nWebsite: {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0,END)
    characters = list(string.ascii_letters)
    numbers = list(string.digits)
    special_symbol = list(string.punctuation)

    password = []
    n = random.randint(10,16)
    for i in range(random.randint(2,4)):
        password.append(random.choice(characters))
    for i in range(random.randint(6,10)):
        password.append(random.choice(numbers))
    while len(password) < n:
        password.append(random.choice(special_symbol))

    random.shuffle(password)
    password = ''.join(password)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = password_entry.get()
    website = www.get()
    user_email = username_entry.get()
    if len(user_email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Input", message="Please fill all fields.")
    else:
        is_ok = messagebox.askokcancel(title=f"Website - {website}", message=f"Is this information correct? :\nEmail: {user_email}\n"
                                                               f"Password: {password}")
        if is_ok:
            data = {website: {"Email": user_email,
                              "Password": password}}
            try:
                with open("data.json", "r") as file:
                    previous_data = json.load(file)
                    previous_data.update(data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(previous_data, file, indent=4)
            finally:
                password_entry.delete(0, END)
                www.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

website = Label(text="Website:", width=10)
email = Label(text="Email/Username:")
password_label = Label(text="Password:")
website.grid(row=1, column=0)
email.grid(row=2, column=0)
password_label.grid(row=3, column=0)

www = Entry(width=35)
www.grid(columnspan=2, row=1, column=1, sticky="W")
www.focus()
username_entry = Entry(width=35)
username_entry.grid(columnspan=2, row=2, column=1, sticky="W")
username_entry.insert(0, "sumitjaidka789@gmail.com")
password_entry = Entry(width=25)
generate_pass = Button(text="Generate Password", command=generate, width=14)
password_entry.grid(row=3, column=1, sticky="W")
generate_pass.grid(row=3, column=2, sticky="W")

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="W")

search_btn = Button(text="Search", command=search, width=14)
search_btn.grid(row=1, column=2)
window.mainloop()

