import turtle
import random

turtle.speed(0)
turtle.colormode(255)
turtle.hideturtle()
turtle.bgcolor("darkslateblue")
paint=["cornsilk","cornsilk1","blueviolet", "purple"]
    
for angle in range(0,330,3):#0 oos 360 graduis hurtel ontsog n 10 r nemegdej bn
    turtle.goto(0,0)
    turtle.color(random.choice(paint))
    turtle.seth(angle)#ontsog n taaruulj bn
    turtle.forward(800)


turtle.done()
