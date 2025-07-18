import turtle
import random

turtle.speed(0)
turtle.colormode(255)
turtle.hideturtle()
paint1=["yellow","darkgoldenrod1","orange"]
paint2=["deepskyblue","cyan","blue"]
for cirkul in range(0,330,3):
    turtle.goto(100,100)
    turtle.color(random.choice(paint1))
    turtle.seth(cirkul )
    turtle.forward(800)

for angle in range(0,330,3):
    turtle.goto(-100,-100)
    turtle.color(random.choice(paint2))
    turtle.seth(angle)
    turtle.forward(800)

turtle.done()