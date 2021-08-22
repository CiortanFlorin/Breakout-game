from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super(). __init__()
        self.speed("slow")
        self.penup()
        self.shape("circle")
        self.color("black")
        self.goto(0, -100)
        self.x=10
        self.y=10

    def move(self):
        new_x=self.xcor()+self.x
        new_y=self.ycor()+self.y
        self.goto(new_x, new_y)


    def bounce_wall(self):
        self.x *= (-1)


    def bounce_ceiling(self):
        self.y *= (-1)

    def ball_reset(self):
        self.x = 10
        self.y = 10
        self.goto(0, -100)