from turtle import Turtle
import random


'''Class to create ball for the Pong Game'''

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.setheading(random.randint(45,135))

    def move(self, speed):
        super().__init__()
        self.forward(speed)
