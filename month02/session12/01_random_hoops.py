import turtle
import  random
turtle.speed(0)

paint=["red","blue","yellow","green"]

for size in range(400, 0,-10):#0 oos 360 graduis hurtel ontsog n 10 r nemegdej bn
    turtle.color(random.choice(paint))
    turtle.dot(size)

turtle.done()