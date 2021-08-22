from turtle import Screen, Turtle
from bar import Bar
from bricks_manager import BricksManager
from ball import Ball
from scoreboard import Scoreboard
import time
rows = range(-380,400,50)
columns = [0, 30, 60, 90]

#Create screen
screen = Screen()
screen.setup(800, 600)
screen.title("Breakout")

#Stop screen from auto-updating
screen.tracer(0)

scoreboard = Scoreboard()
bar = Bar()
ball = Ball()
#Make screen react to keyboard press of a and d
screen.listen()
screen.onkey(bar.move_left, "a")
screen.onkey(bar.move_right, "d")


bricks={}
#A function witch makes a dictionary of brick objects
def lay_bricks():
    i=0
    for c in columns:
        color=int(c/30)
        for n in rows:
            bricks[i]=BricksManager(n,c,color)
            i+=1

score=0
lay_bricks()
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)

    ball.move()
    #Wall bounce
    if ball.xcor() < -380 or ball.xcor() > 380 :
        ball.bounce_wall()
    #Ceiling and bar bounce
    if ball.ycor() > 280 or ball.distance(bar)<40:
        ball.bounce_ceiling()
    #Aparent deletion of a brick
    for brick in bricks:
        if ball.distance(bricks[brick])<30:
            bricks[brick].speed("fastest")
            bricks[brick].goto(900,900)
            ball.bounce_ceiling()
            if brick < 32:
                score+=5
            else:
                score+=7
            scoreboard.score_points(score)
    #Behaviour for losing the game
    if ball.ycor() < -280:
        score=0
        scoreboard.score_points(score)
        for brick in bricks:
            bricks[brick].speed("fastest")
            bricks[brick].goto(900, 900)
        lay_bricks()
        ball.ball_reset()


screen.exitonclick()