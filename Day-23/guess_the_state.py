import pandas
from turtle import Turtle,Screen,shape

screen = Screen()
screen.title("INDIA STATE GAME")
screen.setup(800,800)
static_image = "E:/python/python udemy/Day-25/india.gif"
screen.addshape(static_image)
shape(static_image)

data = pandas.read_csv("E:/python/python udemy/Day-25/state_name.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 34:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/28 GUESS THE STATE",prompt="What's the another state's name?") 

    if answer_state == "exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("E:/python/python udemy/Day-25/state_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()
