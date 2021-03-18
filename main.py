from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()

screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Paddle(350)

AI = Paddle(-350)

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
