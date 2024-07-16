from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class GUI():
    def __init__(self,quiz_brain:QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QUIZ BRAIN")
        self.window.minsize(width=400,height=450)
        self.window.config(padx=20,pady=20,background=THEME_COLOR)

        self.canva = Canvas(width=400,height=420,highlightthickness=0)
        

        #True imaage and button
        self.true_img = PhotoImage(file="E:/Python Udemy/Day-34/images/true.png")
        self.true_button = Button(text="Add",width=100,image=self.true_img,command=self.true_answer)
        self.true_button.grid(column=0,row=2)

        #False static/image and button
        self.false_img = PhotoImage(file="E:/Python Udemy/Day-34/images/false.png")
        self.false_button = Button(text="Add",width=100,image=self.false_img,command=self.false_answer)
        self.false_button.grid(column=1,row=2)
        
        #adding the question in the canva
        self.Que = self.canva.create_text(200,210,text="question",width=380,font=("Arial",20,"bold"))

        #scores 
        self.Scores = Label(text=f"Score:0",font=("Arial",15,"bold"),bg=THEME_COLOR,fg="white")
        self.Scores.grid(column=1,row=0)
        self.canva.grid(column=0,row=1,columnspan=2,padx=30,pady=30)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question (self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():
            self.Scores.config(text=f"Score:{self.quiz.score}")
            question_text =  self.quiz.next_question()
            self.canva.itemconfig(self.Que, text = question_text)
        else:
            self.canva.itemconfig(self.Que,text = "You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
         self.feed_back(is_right =  self.quiz.check_answer("True"))
       

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.feed_back(is_right)

    def feed_back(self,is_right):
        if is_right:
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.window.after(1000,self.get_next_question,)
        
