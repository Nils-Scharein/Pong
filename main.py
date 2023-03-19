import time
from turtle import Turtle, Screen
from Scoreboard import Scoreboard
from Ball import Ball
from Player import Player

#setup variablen
HEIGHT = 800
WIDTH = 1200
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DISTANCE = 50


#setup main screen
screen = Screen()
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)

score = Scoreboard(HEIGHT, WIDTH)
screen.tracer(0)

def dotted(long):
    line = Turtle()
    line.penup()
    line.color("white")
    line.hideturtle()
    line.setpos(0, HEIGHT/2)
    line.setheading(DOWN)
    while line.ycor() > -(HEIGHT/2):
        line.pendown()
        line.fd(long)
        line.up()
        line.fd(long)
        line.down()



def set_heading():
    screen.onkeypress(player1.up(), "w")
    screen.onkeypress(player1.down(), "s")
    screen.onkeypress(player2.up(), "UP")
    screen.onkeypress(player2.down(), "DOWN")


score = Scoreboard(HEIGHT, WIDTH)
ball = Ball(HEIGHT, WIDTH)
player1 = Player(HEIGHT, WIDTH, (-(WIDTH / 2) + DISTANCE, 0))
player2 = Player(HEIGHT, WIDTH, ((WIDTH / 2) - DISTANCE, 0))

def main():
    dotted(10)
    score.draw_score()
    ball.random_start()
    set_heading()
    while True:
        screen.update()
        ball.move(10)
        ball.score_goal(score)
        ball.change_directions()
        time.sleep(0.02)

screen.listen()
main()
screen.exitonclick()
