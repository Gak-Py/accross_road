from turtle import Turtle
import random
START_POSITION = (0, -280)

class Tim(Turtle):

    def __init__(self):
        super(Tim, self).__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.start()
        self.goto(START_POSITION)

    def start(self):
        self.goto(random.randint(-200, 200), -280)

    def move(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
