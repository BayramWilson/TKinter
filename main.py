from tkinter import *


window = Tk()
window.title("Miles to km")
window.minsize(width=150, height=100)
window.config(padx=20, pady=20)


miles = Label(text="Miles", font=("Arial", 12, "bold"))
miles.grid(column=2, row=0)

equal_to = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_to.grid(column=0, row=1)

solution = Label(text="0", font=("Arial", 12, "bold"))
solution.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 12, "bold"))
km.grid(column=2, row=1)


entry = Entry()
entry.insert(END, string="0")
entry.grid(column=1, row=0)


def miles_to_kilometre():
    str_entry = entry.get()
    int_entry = float(str_entry)
    int_entry *= 1.6
    solution.config(text=int_entry)


def convert_button_clicked_miles_to_kilometre():
    if km.grid(column=2, row=1) == km.grid(column=2, row=1):
        miles.grid(column=2, row=1)
        km.grid(column=2, row=0)
        button.config(command=kilometre_to_miles)
        convert_button.config(command=convert_button_clicked_kilometre_to_miles)


def kilometre_to_miles():
    str_entry = entry.get()
    int_entry = float(str_entry)
    int_entry /= 1.6
    solution.config(text=int_entry)


def convert_button_clicked_kilometre_to_miles():
    if km.grid(column=2, row=0) == km.grid(column=2, row=0):
        km.grid(column=2, row=1)
        miles.grid(column=2, row=0)
        button.config(command=miles_to_kilometre)
        convert_button.config(command=convert_button_clicked_miles_to_kilometre)


button = Button(text="Calculate", command=miles_to_kilometre)
button.grid(column=1, row=2)

# convert button

convert_button = Button(text="convert", command=convert_button_clicked_miles_to_kilometre)
convert_button.grid(column=2, row=2)

window.mainloop()
