from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


#ALL_SPEED = 8

screen = Screen()

screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Paddle(350)

AI = Paddle(-350)

ball  = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(AI.go_up, "w")
screen.onkey(AI.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    #detect vertical collision, invert vertical movement
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.vertical_collision()

    #detect paddle collision, invert horizontal movement
    if (ball.xcor() == 330 and ball.distance(player) < 50) or (ball.xcor() == -330 and ball.distance(AI) < 50):
        ball.paddle_collision()

    #detect score player
    if ball.xcor() < -390:
        scoreboard.player_score +=1
        scoreboard.clear()
        scoreboard.update_scoreboard()
        ball.reset_ball()

    #detect score AI
    if ball.xcor() > 390:
        scoreboard.AI_score +=1
        scoreboard.clear()
        scoreboard.update_scoreboard()
        ball.reset_ball()


screen.exitonclick()
