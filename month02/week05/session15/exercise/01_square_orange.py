import turtle

turtle.speed(0)

def drawSquare(x,y,w,color):
    turtle.goto(x,y)
    turtle.width(6)
    turtle.color(color,color)
    turtle.begin_fill()

    for n in range (4):
        turtle.penup()
        turtle.fd(w)
        turtle.rt(90)
        turtle.penup()

    turtle.end_fill()

    if color=='orange':
        color='black'
    else:
        color='orange'
    if w>200:
        drawSquare(x, y , w-35,color)

drawSquare(0,0,400,'orange')

turtle.done()