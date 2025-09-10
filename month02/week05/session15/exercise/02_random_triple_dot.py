import turtle
import random

turtle.speed(0)
turtle.penup()
turtle.hideturtle()

    
def circle(x, y, w, color):
    turtle.goto(x, y)
    turtle.dot(w, color)

    if color == "red":
        color = "orange"
    else: color = "yellow"
        
        
    # Recursive call
    if w > 40:
        circle(x , y , w -40, color)


for l in range(0,600):
    x= random.randint(-600,600)
    y= random.randint(-600,600)
    circle(x, y, 200, 'red')

turtle.done()
