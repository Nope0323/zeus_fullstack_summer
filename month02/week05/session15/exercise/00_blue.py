import turtle


def drawSpiral(side):
    turtle.fd(side)
    turtle.rt(45)
    if side >10:
        drawSpiral(side-5)

turtle.color('blue')
turtle.width(15)

drawSpiral(120)


turtle.done()