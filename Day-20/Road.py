from turtle import Turtle

x_position = [-70,-40,-10,20,50,80]

class Road(Turtle):
    def __init__(self,new_x,new_y) -> None:
        super().__init__()
        self.x = new_x
        self.y = new_y
        self.color("white")
        self.left(90)
        self.shape("square")
        self.shapesize(0.2,3)
        self.penup()
        self.left(90)
        self.speed("fastest") 
        self.goto(self.x,self.y)

            
            
            

