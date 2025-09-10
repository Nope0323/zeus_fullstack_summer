import turtle
import random

turtle.penup()
turtle.speed(0)
turtle.colormode(255)

for c in range(0,225):
    x= random.randint(-200,200)
    y= random.randint(-200,200)
    turtle.goto(x,y)
    turtle.color(255,c,0)
    turtle.dot(20)

turtle.done()