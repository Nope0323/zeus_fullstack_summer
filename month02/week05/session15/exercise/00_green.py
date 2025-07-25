import turtle


def drawSpiral(side):
    turtle.fd(side)
    turtle.rt(90)
    if side >10:
        drawSpiral(side-7)

turtle.color('green')
turtle.width(5)

drawSpiral(180)


turtle.done()