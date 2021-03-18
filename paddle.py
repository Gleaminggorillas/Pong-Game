from turtle import Turtle

paddle = Turtle()

class Paddle:
    
    def __init__(self):
        self.paddle = Turtle()

    def create_paddle(self):

        paddle.color("white")
        paddle.penup()
        paddle.shape("square")
        paddle.shapesize(stretch_len=1, stretch_wid=5)
        paddle.goto(350, 0)

    def go_up(self):
        new_y = paddle.ycor() + 20
        paddle.goto(paddle.xcor(), new_y)

    def go_down(self):
        new_y = paddle.ycor() - 20
        paddle.goto(paddle.xcor(), new_y)

