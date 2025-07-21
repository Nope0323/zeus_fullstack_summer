
step = 0 
tired = False
bad_weather=False

while step <10000:
    if tired == True:
        break
    elif bad_weather == True:
        break
    else:
        step=step+1

print('out of the while loop!')

x=45
y=80

while x<50 and y<100:
    x=x+1
    y=y+1

    print(x,y)

x=0 
while x<20:
    print (f'hello{x}')
    if x<9:
        break
