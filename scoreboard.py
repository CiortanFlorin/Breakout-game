from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super(). __init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-350, 270)
        self.write("Score: 0", align="center", font=("Arial", 16, "normal"))

    def score_points(self, x):
        self.clear()
        self.write(f"Score: {x}", align="center", font=("Arial", 16, "normal"))