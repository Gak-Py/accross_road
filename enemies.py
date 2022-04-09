from turtle import Turtle
import random


class Enemies(Turtle):
    def __init__(self):
        super(Enemies, self).__init__()
        self.shape("turtle")
        self.penup()
        col_r = random.randint(100, 255)
        col_g = random.randint(100, 255)
        col_b = random.randint(100, 255)
        random_y = random.randint(-250, 250)
        self.color(col_r, col_g, col_b)
        self.setheading(180)
        self.goto(300, random_y)

    def move(self):
        new_x = self.xcor() - random.randint(4, 20)
        self.goto(new_x, self.ycor())

    def appear(self):
        self.goto(300, random.randint(-250, 250))