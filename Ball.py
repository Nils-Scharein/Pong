from turtle import Turtle
import random
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Ball():
    def __init__(self, HEIGHT, WIDTH):
        self.turtle = self.setup_turtle()
        self.height = HEIGHT
        self.width = WIDTH

    def setup_turtle(self):
        local_turtle = Turtle()
        local_turtle.penup()
        local_turtle.color("white")
        local_turtle.shape("circle")
        local_turtle.speed("fastest")
        return local_turtle

    def move(self, SPEED):
        self.turtle.fd(SPEED)
        self.change_directions()

    def random_start(self):
        a = True
        while a:
            r = random.randint(0, 360)#
            if random == 180 or random == 90:
                pass
            else:
                self.turtle.setpos(0,0)
                self.turtle.rt(r)
                break

    def change_directions(self):
        if (self.turtle.xcor() <= -(self.width/2) and UP <= self.turtle.heading() <= DOWN) or ((self.width/2) <= self.turtle.xcor() and not UP <= self.turtle.heading() <= DOWN):
            self.turtle.left(LEFT - 2 * self.turtle.heading())
        elif (self.turtle.ycor() <= -(self.height/2) and self.turtle.heading() >= LEFT) or ((self.height/2) <= self.turtle.ycor() and self.turtle.heading() <= LEFT):
            self.turtle.left(-2 * self.turtle.heading())

    def score_goal(self, Scoreboard):
        if self.turtle.xcor() < -(self.width/2) + 20:
            Scoreboard.increase_scorep2()
            time.sleep(1)
            self.random_start()
        elif self.turtle.xcor() > (self.width/2) - 20:
            Scoreboard.increase_scorep1()
            time.sleep(1)
            self.random_start()
        else:
            pass
