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

    if color=='blue':
        color='yellow'
    else:
        color='blue'
    if w>20:
        drawSquare(x+10, y -10, w-20,color)

drawSquare(0,0,400,'blue')

turtle.done()