import turtle

turtle.colormode(255)
turtle.speed(0)
for a in range(255,0,-10):
    turtle.color(255-a,0,0) # (255,255,5) (245,245,5)
    turtle.dot(a) # (255) (245)

turtle.done()