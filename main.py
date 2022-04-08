from turtle import Turtle, Screen
from tim import Tim
from msg import Msg
from enemies import Enemies
import random
import time

tim = Tim()
msg = Msg()
screen = Screen()
screen.colormode(255)
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

enemies_list = []

screen.listen()
screen.onkey(tim.move, "Up")

difficulty = [0,1,0]

game_on = True
while game_on:
    print(len(enemies_list))
    for i in range(random.choice(difficulty)):
        enemies = Enemies()
        enemies_list.append(enemies)

    for enemie in enemies_list:
        random_walk = random.randint(4, 20)
        enemie.move(random_walk)
        if enemie.xcor() <= -330:
            enemies_list.remove(enemie)

        if tim.distance(enemie) <= 20:
            msg.game_over()
            game_on = False

    time.sleep(0.1)
    screen.update()
    if tim.ycor() >= 300:
        msg.goal()
        for enemie in enemies_list:
            enemie.goto(-320, enemie.ycor())
        if len(difficulty) <= 8:
            difficulty.append(1)
        else:
            difficulty.append(random.randint(1,2))
        tim.start()

screen.exitonclick()