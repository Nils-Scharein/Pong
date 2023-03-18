from turtle import Turtle, Screen
from Scoreboard import Scoreboard



class Ball():

    def __init__(self):
        self.turtle = self.setup_turtle()

    def setup_turtle(self):
        local_turtle = Turtle()
        local_turtle.penup()
        local_turtle.color("white")
        local_turtle.shape("square")
        local_turtle.speed("fastest")
        return local_turtle

    def move(self):
        self.turtle.fd(20)

    def random_start(self):
        pass
