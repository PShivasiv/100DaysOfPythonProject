from turtle import Turtle,Screen
import random

screen = Screen()
screen.screensize(500,400)
user_choice = screen.textinput(title="Make a bet",prompt="Enter a color which you thought to win")

turtle_list = ["red","green","yellow","blue","orange","purple"]
y_position = [-70,-40,-10,20,50,80]
forward = [0,1,2,3,4,5,6,7,8,9,10]
all_turtle =[]
#players
if user_choice:
    is_race_on = True


for turtle_index in range(0,6):
    red = Turtle("turtle")
    red.color(turtle_list[turtle_index])
    red.penup()
    red.goto(-365,y_position[turtle_index])
    all_turtle.append(red)

    
while is_race_on:
    for turtles in all_turtle:
        forwords = random.randint(0,10)
        turtles.forward(forwords)
        winning_color = turtles.pencolor()
        if turtles.xcor() > 365:
            is_race_on = False
            if winning_color == user_choice:
                print(f"your bet is right you won the 10000 rupees. The WINNING COLOR IS {winning_color}")
            else:
                print(f"Sorry you loss you have to pay 100 rupees. The WINNING COLOR IS {winning_color}")


screen.exitonclick()
