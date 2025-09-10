import turtle

turtle.speed(0)
side_num = 6
side_length = 70

angle = 360 / side_num


for i in range(side_num):
    turtle.forward(side_length)
    turtle.right(angle)
    


turtle.done()