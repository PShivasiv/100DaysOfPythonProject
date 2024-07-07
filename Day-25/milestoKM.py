from tkinter import *

window = Tk()
window.minsize(width=200,height=200)
window.title("Mile to KM Converter")


miles = Label(text="Miles",font=("Arial",10,"normal"))
miles.grid(column=2,row=0)
miles.config(padx=5,pady=5)

km = Label(text="Km",font=("Arial",10,"normal"))
km.grid(column=2,row=1)
km.config(padx=5,pady=5)

equal = Label(text="is equal to",font=("Arial",10,"normal"))
equal.grid(column=0,row=1)
equal.config(padx=5,pady=5)

input = Entry(width=10,font=("Arial",10,"normal"))
input.grid(column=1,row=0)

answer = Label(text=0,font=("Arial",10,"normal"))
answer.grid(column=1,row=1)

def button_click():
    n = float(input.get())
    kilo = round(n * 1.609344)
    answer.config(text=kilo)

button = Button(text="Calculate",command=button_click,font=("Arial",10,"normal"))
button.grid(column=1,row=3)
# input.config(padx=5,pady=5)


window.mainloop()
