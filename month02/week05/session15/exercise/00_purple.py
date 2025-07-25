import turtle


def drawSpiral(side):
    turtle.fd(side)
    turtle.rt(35)
    if side >10:
        drawSpiral(side-5)

turtle.color('purple')
turtle.width(5)

drawSpiral(180)


turtle.done()