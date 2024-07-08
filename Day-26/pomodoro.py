from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
PURPLE = "#E49BFF"
YELLOW = "FFDB00"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_time = None


# ---------------------------- TIMER MECHANISM ------------------------------- # 

    


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

       
    if reps % 2 == 0:
        count_down(short_break)
        timer.config(text="BREAK")
     
    elif reps == 8:
        count_down(long_break)
        timer.config(text="BREAK")

    else:
        count_down(work_sec)
        timer.config(text="WORK")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor( count / 60)
    count_sec = count % 60

    if count_sec == 10:
        count_sec = f"0{count_sec}"

    if count > 0:
        canva.itemconfig(Timer_text,text = f"{count_min}:{count_sec}")
        global my_time 
        my_time = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_time)
    canva.itemconfig(Timer_text,text = "00:00")
    timer.config(text="Timer")
    check.config(text="")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(width=500,height=500)
window.config(padx=100,pady=100,bg=PURPLE)
# window.after(1000,) # This function take the miliesecond as a time and the function which gonna exicute after that time

# There is  a another method to print the static/image in window
# img = Photostatic/image(file='E:/python/python udemy/Day-28/tomato.png')
# Label(
#     static/image=img,
#     font=("Arial",23,"normal"),
#     text="00:00"
# ).pack()


canva = Canvas(width=200,height=224,bg=PURPLE,highlightthickness=0)
tomato_img = PhotoImage(file="E:/python/python udemy/Day-28/tomato.png")
canva.create_image(100, 112, image=tomato_img)

Timer_text = canva.create_text(100,130,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")
canva.grid(column=1,row=1)


start_button = Button(text="Start",command=start_timer)
start_button.config(padx=10,pady=5)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.config(padx=10,pady=5)
reset_button.grid(column=2,row=2)



timer = Label(text="Timer",fg=RED,font=(FONT_NAME,34,"bold"),background=PURPLE)
timer.grid(column=1,row=0)


check = Label(fg=GREEN,background=PURPLE,font=(FONT_NAME,50,"bold"))
check.grid(column=1,row=4)




window.mainloop()
