from turtle import Turtle, Screen
from paddle import Paddle

turtle = Turtle()

screen = Screen()

player = Paddle()

screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")

player.create_paddle()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

'''def go_up():
    new_y = player.ycor() + 20
    player.goto(player.xcor(), new_y)

def go_down():
    new_y = player.ycor() - 20
    player.goto(player.xcor(), new_y)'''

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

screen.exitonclick()
