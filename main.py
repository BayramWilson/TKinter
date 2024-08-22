from tkinter import *


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

#Labels

miles = Label(text="Miles", font=("Arial", 24, "bold"))
miles.grid(column = 2, row=0)

equal_to = Label(text="is equal to", font=("Arial", 24, "bold"))
equal_to.grid(column = 0, row=1)

solution =Label(text="0", font=("Arial", 24, "bold"))
solution.grid(column = 1, row=1)

km = Label(text="Km", font=("Arial", 24, "bold"))
km.grid(column = 2, row=1)


entry = Entry()
entry.insert(END, string="0")

#Button

def button_clicked():

    solution.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.grid(column= 2, row= 1)



#Entry(input field)

input = Entry(width=10)
input.grid(column= 3, row= 2)
print(input.get())


window.mainloop()