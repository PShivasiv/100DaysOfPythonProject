from turtle import Turtle,Screen
from move_paddle import Paddle
from move_ball import Move
import time
from score_board import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("PONG GAME")
screen.setup(800,600)
screen.tracer(0)


paddle_1 = Paddle((350,0))
paddle_2 = Paddle((-350,0))
ball_1 = Move()
score = ScoreBoard()


screen.listen()

screen.onkeypress(paddle_1.Turn_up,"Up")
screen.onkeypress(paddle_1.Turn_down,"Down")
screen.onkeypress(paddle_2.Turn_up,"w")
screen.onkeypress(paddle_2.Turn_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball_1.ball_speed)
    screen.update()
    ball_1.ball_move()
#detection and bounce back the ball
    if ball_1.ycor() > 280 or ball_1.ycor() < -280:
        ball_1.bounce()
#collision with paddle
    if ball_1.distance(paddle_1) < 50 and ball_1.xcor() > 320 or ball_1.distance(paddle_2) < 50 and ball_1.xcor() < -320:
        ball_1.bounce_paddle()
#Collision with the wall
    if ball_1.xcor() > 350:
        score.increase_score_left()
        ball_1.reset()
    if ball_1.xcor() <-350:
        score.increase_score_right()
        ball_1.reset()
#increase the ball speed 
    




screen.exitonclick()
