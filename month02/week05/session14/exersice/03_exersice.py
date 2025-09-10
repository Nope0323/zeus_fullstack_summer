import turtle

def square(x, y,size , color):
    turtle.speed(0)
    turtle.color(color)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for a in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
square(-500,400,800, 'yellow')
square(-400, 300,200,'white')
square(-300, 200,100,'black')
square(-20, 300,200,'white')
square(80, 200,100,'black')
square(-300,-100,200, 'red')
square(-200,-10,200, 'yellow')







turtle.done()