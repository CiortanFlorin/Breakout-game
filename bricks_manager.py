from turtle import Turtle

COLORS = ["yellow", "green", "orange", "red"]

class BricksManager(Turtle):

    def __init__(self, x, y, z):
        super(). __init__()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.shapesize(1, 2, 1)
        self.color(COLORS[z])
        self.seth(180)
        self.goto(x,y)

