from turtle import Turtle
import random
import time

class Move(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.shape("circle")
        self.shapesize(1,1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def ball_move(self):
        position_x = self.xcor() + self.x_move
        position_y = self.ycor() + self.y_move
        self.goto(position_x,position_y)

    def bounce(self):
        self.y_move *= -1
    def bounce_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
    def reset(self):
        self.goto(0,0)
        self.ball_speed = 0.1
