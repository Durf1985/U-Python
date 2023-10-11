from tkinter import *
import playground


def button_clicked(event=None):
    miles_to_km = round(int(how_miles.get()) * 1.6, 2)
    result.config(text=str(miles_to_km))


window = Tk()
window.title("First Gui")
window.minsize(600, 400)
window.config(padx=300, pady=200)

how_miles = Entry(width=10)
how_miles.grid(column=1, row=0)
how_miles.focus()
how_miles.bind("<Return>", button_clicked)
how_miles.bind("<KP_Enter>", button_clicked)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_eq = Label(text="is equal to")
is_eq.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)

window.mainloop()
