from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 1
        self.color("white")
        self.penup()
        self.goto(-300,250)
        self.hideturtle()
        self.write(f"Level:{self.score}",align="center",font=("Arial", 20 , "normal"))
        self.car_speed = 0.2
        

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level:{self.score}",align="center",font=("Arial", 20 , "normal"))
        self.car_speed *= 0.9
    def game_over(self):
        self.goto(0,50)
        self.clear()
        self.write("GAME OVER",align="center",font=("Arial", 30 , "normal"))
        self.car_speed = 0.2
