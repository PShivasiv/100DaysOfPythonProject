from tkinter import *
from tkinter import messagebox
import pyperclip
import json

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
PURPLE = "#E49BFF"
YELLOW = "FFDB00"
FONT_NAME = "Courier"

# --------------------PASSWORD GENERATOR-------------------- #

import random
def random_generater():
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
          'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|' ]
 
    password_symbol = [random.choice(symbols) for char in range(random.randint(2,4))]
    password_letter = [random.choice(letter) for char in range(random.randint(8,10))]
    password_digit = [random.choice(digits) for char in range(random.randint(2,4))]

    password_list = password_symbol + password_letter + password_digit
    random.shuffle(password_list)

    password = "".join(password_list)  #This is the function to join the two or three string together 
    password_input.delete(0,END)
    password_input.insert(0,password)
    pyperclip.copy(password)


# --------------------SAVE PASSWORD ------------------------ #
def save():
    website = web_input.get()
    email = user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password
        }
    }


    if website == "": 
        emty_web = messagebox.showerror(title="Website Name is missing",message="You have to enter the website name to proceed")
    elif password == "":
        empty_password = messagebox.showerror(title="Password is missing",message="You have to enter the Password to proceed")
    else:
        is_ok = messagebox.askokcancel(title=website , message=f"These are the details entered:\n Email : {email}\n Password : {password}\n Is it ok to save?")
        try:
            if is_ok:
                with open("E:/python/python udemy/Day-29/data.json","r") as datafile:

                    data = json.load(fp=datafile)  #reading the data
            
        except FileNotFoundError:
            with open("E:/python/python udemy/Day-29/data.json","w") as datafile:
                json.dump(new_data,datafile,indent=4) # now finally write the data in the json file
                pyperclip.copy(password)

        else:

            data.update(new_data) # updating the new data in the json file
            with open("E:/python/python udemy/Day-29/data.json","w") as datafile:

                json.dump(data,datafile,indent=4)
                pyperclip.copy(password)

        finally:
                    web_input.delete(0,END)
                    password_input.delete(0,END)

# --------------------FINDING FILE ----------------------------- #

def find_password():
    website =web_input.get()
    try:
        with open("E:/python/python udemy/Day-29/data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="FileNotFound",message="NO data in the file")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email : {email}\n Password : {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details of {website} exists.")
# --------------------UI SETUP ----------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=500,height=500)
window.config(padx=40,pady=40,bg=PURPLE)

canva = Canvas(width=270,height=220,bg=PURPLE,highlightthickness=0)
lock_img = PhotoImage(file="E:/python/python udemy/Day-29/logo.png")
canva.create_image(100,110,image = lock_img)
canva.grid(column=1,row=0,columnspan=2)

#lables

website_name = Label(text="Website:",background=PURPLE)
website_name.config(padx=10,pady=10)
website_name.grid(column=0,row=1)

user_name = Label(text="Email/Username:",background=PURPLE)
user_name.grid(column=0,row=2)
user_name.config(padx=10,pady=10)

pass_lable = Label(text="Password:",background=PURPLE)
pass_lable.grid(column=0,row=3)
pass_lable.config(padx=10,pady=10)

#inputs
web_input = Entry(width=25,font=12)
web_input.grid(column=1,row=1)


user_input = Entry(width=39,font=12)
user_input.grid(column=1,row=2,columnspan=2)
user_input.insert(END,"@email.com")

password_input = Entry(width=25,font=12)
password_input.grid(column=1,row=3,)

#buttons

search = Button(text="Search",width=17,command=find_password)
search.grid(column=2,row=1)


generate = Button(text="Generate Password",width=17,command=random_generater)
generate.grid(column=2,row=3)

add = Button(text="Add",width=40,font=10,command = save)
add.grid(column=1,row=4,columnspan=2)


window.mainloop()
