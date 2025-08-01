import turtle
import random

turtle.speed(0)
turtle.penup()
turtle.hideturtle()

    
def circle(x, y, w, color):
    turtle.goto(x, y)
    turtle.dot(w, color)

    if color == "purple":
        color = "black"
    elif color == "red":
        color=="purple"
    elif  color=="red":
        color=="pink"
    elif  color=="blue":
        color=="dark blue"
    else: 
        color = "purple"
        
        
    # Recursive call
    if w > 10:
        circle(x , y , w -40, color)



    
circle(0, 0, 200, 'red')

turtle.done()

turtle.done()