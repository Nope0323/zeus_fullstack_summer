import turtle
import random

turtle.speed(0)
turtle.colormode(255)
turtle.hideturtle()
paint2=["deepskyblue","cyan","blue"]

for angle in range(0,360,3):
    turtle.goto(180,190)
    turtle.color(random.choice(paint2))
    turtle.seth(angle)
    turtle.forward(1000)

turtle.done()