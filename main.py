import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from decoration import Decoration
from speedometer import Speedometer
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=700)
screen.title("Pong")

screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()
decoration = Decoration()
speedometer = Speedometer(ball.move_speed)

screen.listen()
screen.onkeypress(r_paddle.go_up, "8")
screen.onkeypress(r_paddle.go_down, "2")

screen.onkeypress(l_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        #needs to bounce
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x() #ball move_speed will increase
        speedometer.update_speed(ball.move_speed)

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position() #ball nove speed will be reset to 0.1
        speedometer.update_speed(ball.move_speed)
        scoreboard.l_point()

    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position() #ball nove speed will be reset to 0.1
        speedometer.update_speed(ball.move_speed)
        scoreboard.r_point()



screen.exitonclick()