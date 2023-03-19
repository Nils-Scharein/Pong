from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
number = 12

class Player():

    def __init__(self, Height, Width, start):
        self.segments = []
        self.height = Height
        self.width = Width
        self.start = start
        self.create_player(start)
        self.upper_player = self.segments[0]
        self.lower_player = self.segments[-1]

    def create_player(self, center):
        x, y = center
        if number % 2 == 0:
            start = ((number // 2) * 20) - 10
            for i in range(0, number):
                print(start)
                turtle = self.create_turtle()
                turtle.color("red")
                print(start)
                turtle.setpos(x, start)
                self.segments.append(turtle)
                start -= 20
        else:
            start = ((number + 1 // 2) * 20) - 20
            for i in range(0, number):
                print(start)
                turtle = self.create_turtle()
                turtle.color("blue")
                turtle.setpos(x, start)
                self.segments.append(turtle)
                start -= 20

    def create_turtle(self):
        local_turtle = Turtle()
        local_turtle.penup()
        local_turtle.color("white")
        local_turtle.shape("square")
        local_turtle.setheading(UP)
        return local_turtle

    def up(self):
        self.upper_player.fd(20)

    def down(self):
        self.lower_player.bk(20)

