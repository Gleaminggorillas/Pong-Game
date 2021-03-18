from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.AI_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 255)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"AI Score = {self.AI_score}  Player Score = {self.player_score}",
                   align=ALIGNMENT,
                   font=FONT)

    def increase_points(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()