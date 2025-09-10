import turtle

a= input("loop number:")
angle_number= input ('give me angle:')

limit_number = int(a)
limit_angle= int(angle_number)
turtle.width(4)
turtle.color('red')
turtle.speed(0)

for i in range(limit_number):
    #turtle.right
    turtle.right(limit_angle)
    for n in range(4):
        turtle.forward(100)
        turtle.right(90)

turtle.done()