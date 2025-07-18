import turtle

turtle.colormode(255)
turtle.speed(0)
for a in range(250,0,-1):
    turtle.color(255,a,0)
    turtle.dot(2*a)

turtle.done()