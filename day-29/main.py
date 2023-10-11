from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def find_password():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    else:
        try:
            password = data[website_entry.get()]["password"]
        except KeyError:
            messagebox.showinfo(title="Oops", message="No details for the website exists.")
        else:
            messagebox.showinfo(title=website_entry.get(), message=f"Website: {website_entry.get()} \n"
                                                                   f"Password: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    overall_string = None

    letter = [random.choice(letters) for _ in range(random.randint(6, 8))]
    symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    sum_list = letter + symbol + number
    random.shuffle(sum_list)
    password_entry.delete(0, END)
    password_entry.insert(0, ''.join(sum_list))
    pyperclip.copy(''.join(sum_list))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    if not all([website_entry.get(), password_entry.get(), email_entry.get()]):
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        new_data = {
            website_entry.get(): {
                "email": email_entry.get(),
                "password": password_entry.get()
            }
        }

        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"These are the details entered: \nEmail: {email_entry.get()} \n"
                                               f"Password: {password_entry.get()} \n"
                                               f"Is it ok to save?", )
        if is_ok:
            try:
                with open("data.json", mode="r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as f:
                    json.dump(data, f, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0, sticky='e')

# Labels
website_title = Label(text="Website: ")
website_title.grid(column=0, row=1)
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()
email_entry = Entry(width=40)
email_entry.insert(0, "durf19851@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="w")

# Buttons
search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(column=2, row=1, sticky="e")
password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(column=2, row=3, sticky="e")
add_password_button = Button(text="Add", width=36, command=save_pass)
add_password_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
