from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


BALL_SPEED = 8

screen = Screen()

screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Paddle(350)

AI = Paddle(-350)

ball  = Ball()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move(speed=BALL_SPEED)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.vertical_collision(speed=BALL_SPEED)


screen.exitonclick()
