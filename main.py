from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


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
    ball.move(speed=8)

screen.exitonclick()
