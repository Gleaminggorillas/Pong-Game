from turtle import Turtle

'''Class to create a paddle for the Pong Game'''

class Paddle(Turtle):
    
    def __init__(self, xcor):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(xcor, 0)

#move upwards on up-arrow key
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

#move downwards on down-arrow key
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
