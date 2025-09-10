import turtle


def drawSpiral(side):
    turtle.fd(side)
    turtle.rt(45)
    if side >10:
        drawSpiral(side-5)

turtle.color('red')
turtle.width(5)

drawSpiral(180)


turtle.done()