from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self,position) -> None:
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(5,1)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def Turn_up(self):
            new_y = self.ycor() + 30
            self.goto(self.xcor(),new_y)
    def Turn_down(self):
            new_y = self.ycor() - 30
            self.goto(self.xcor(),new_y) 
     
      
        
        
            
    
