import turtle
import random

turtle.speed(0)
turtle.penup()

paint=["yellow","darkgoldenrod1","orange","red"]
for b in range(0,400):
     x=random.randint(0,400)
     y=random.randint(0,400)

     turtle.goto(x,y)
     for a in range(250,0,-10):
        
        turtle.color(random.choice(paint))
        turtle.dot(a)
       
turtle.done()
