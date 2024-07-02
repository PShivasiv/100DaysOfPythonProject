from turtle import Turtle
import random
STARTING_MOVING = 90
MOVE_INCREMENT = 10
car_color = ["red","green","yellow","blue","orange","purple"]
RANDOM_Y_POSITION = [-110,-25,70,155]

class CarManager():
    def __init__(self) -> None:
        self.all_car = []
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(1,2)
            car.penup()
            car.color(random.choice(car_color))
            random_y = random.choice(RANDOM_Y_POSITION) 
            car.goto(450,random_y)
            self.all_car.append(car)

    def move_car(self):
        for self.car in self.all_car:
            self.car.backward(STARTING_MOVING)
