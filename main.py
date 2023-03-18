import time
from turtle import Turtle, Screen
from Scoreboard import Scoreboard

#setup variablen
HEIGHT = 800
WIDTH = 1200
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
TILE = 16

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

def move():
    line.fd(100)
    line.left(90)

def main():
    dotted(10)
    score.draw_score()
    while True:
        screen.update()
        score.increase_scorep1()
        score.increase_scorep2()
        time.sleep(0.2)

score = Scoreboard(HEIGHT, WIDTH)


screen.listen()


main()
screen.exitonclick()