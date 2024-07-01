from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(50,250)
        self.write(self.score_l,align="center",font=("Arial", 24 , "normal"))
        self.goto(-50,250)
        self.write(self.score_r,align="center",font=("Arial", 24 , "normal"))

    
    def increase_score_left(self):
        self.score_r += 1
        self.update_scoreboard()
    def increase_score_right(self):
        self.score_l += 1
        self.update_scoreboard()
        
    
