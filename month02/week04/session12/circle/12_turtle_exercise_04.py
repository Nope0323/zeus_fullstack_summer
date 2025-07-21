import turtle
import random

turtle.speed(0)
turtle.colormode(255)
turtle.hideturtle()
turtle.width(7)
paint1=["yellow","darkgoldenrod1","orange", "red"]
for cirkul in range(0,360,1):
    turtle.goto(100,100)
    turtle.color(random.choice(paint1))
    turtle.seth(cirkul )
    turtle.forward(800)
turtle.done()