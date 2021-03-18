from turtle import Turtle


'''Class to create ball for the Pong Game'''

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def move(self, speed):
        new_x = self.xcor()+speed
        new_y = self.ycor()+speed
        self.goto(new_x, new_y)

    def vertical_collision(self, speed):
        new_x = self.xcor()+speed
        new_y = self.ycor()-abs(speed)
        self.goto(new_x, new_y)