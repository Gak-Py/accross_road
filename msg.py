from turtle import Turtle
import time

class Msg(Turtle):
    def __init__(self):
        super(Msg, self).__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.level_num = 1
        self.display_level()

    def game_over(self):
        self.write("Game Over.", font=("Futura", 20, "bold"), align="center")

    def goal(self):
        self.goto(0, 0)
        self.clear()
        self.write("Goal!!", font=("Futura", 20, "bold"), align="center")
        time.sleep(2)
        self.clear()
        self.level_num += 1
        self.write(f"Level {self.level_num}", font=("Futura", 40, "bold"), align="center")
        time.sleep(2)
        self.clear()

    def display_level(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level {self.level_num}", font=("Futura", 40, "bold"), align="left")