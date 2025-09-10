
age= input(' age:')

age = int(age) 
if age >=0 and age <=12:
    print('You are baby')
elif age >=13 and age <=19:
    print('You are teenager')
elif age >=20 and age <=65:
    print('You are adult')
elif age >=66 and age <=99:
    print('You are senior')
else:
    print('You are dinosaur')

