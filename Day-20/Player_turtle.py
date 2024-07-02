from turtle import Turtle

class P_turtle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("green")
        self.left(90)
        self.shape("turtle")
        self.shapesize(2,2)
        self.penup()
        self.goto(0,-260)
        self.Turn_up()

    def Turn_up(self):
        new_y = self.ycor() + 30
        self.goto(0,new_y)
    def Turn_down(self):
        new_y = self.ycor() - 30
        self.goto(0,new_y) 
