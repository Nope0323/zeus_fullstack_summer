import turtle
import random

turtle.colormode(255)
turtle.speed(0)

paint=["yellow","darkgoldenrod1","orange", "red"]

for a in range(250,0,-10):
    turtle.goto(0,0)
    turtle.color(random.choice(paint))
    turtle.dot(a)

for b in range(250,0,-10):
    turtle.goto(160,0)
    turtle.color(random.choice(paint))
    turtle.dot(b)
    
turtle.done