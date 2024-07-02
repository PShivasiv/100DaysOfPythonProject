from turtle import Turtle,Screen
from Player_turtle import P_turtle
from Road import Road
from scoreboard import ScoreBoard
import time
from car_manager import CarManager
#road line

new_x = 350
new_y = -250
difficulty = 5
distance = 90 

screen = Screen()
screen.bgcolor("black")
screen.title("CROSS THE ROAD")
screen.setup(800,600)
screen.tracer(0)

player_turtle = P_turtle()
score = ScoreBoard()
carmanager = CarManager()


#Create a road line
for _ in range(0,difficulty):
    new_y += distance
    for _ in range(0,8):
        road = Road(new_x,new_y)
        new_x -= 100   
    new_x = 350

screen.listen()
screen.onkeypress(player_turtle.Turn_up,"Up")
screen.onkeypress(player_turtle.Turn_down,"Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(score.car_speed)
 
# if turtle collision with up wall the level with increase and the line got updated
 
    if player_turtle.ycor() > 260 or player_turtle.ycor() < -270:
        player_turtle.goto(0,-260)
        score.increase_score()
    
    carmanager.create_car()
    carmanager.move_car()

    for car in carmanager.all_car:
        if car.distance(player_turtle) < 20:
            game_is_on = False
            score.game_over()



screen.exitonclick()
