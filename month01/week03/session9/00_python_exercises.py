#Exercice01
num= 7

print(num)

#Exercice02
#. Swap values
#Given two variables, a = 5 and b = 8, swap their values using a temporary variable.
#a = 5, b = 8 гэсэн 2 хувьсагч байгаа бол тэдний утгуудыг түр хувьсагч ашиглан соль.
num_a=5
num_b=8

v = num_a
num_a = num_b
num_b = v

print(num_a, num_b)

#Exercice03

num_x=15
num_y=25

total=15+25

print(total)

#Exercice04

name="Boldo"

print(type(name))

#Exercice05

length = 10 
width = 5

area=length*width

print(area)

#Exercice06

score= 42
plus= score+8

print(plus)

#Exercice07


num_c,num_d,num_e=3,6,9

print(num_c,num_d,num_e)

#Exercice08

is_sky_blue = True


print(is_sky_blue)

#Exercice09

color= "red, blue, green"

print ("My favorite color is ",color)

#Exercice10
integer=3.7
num_t=4

result= integer+num_t
print(type(result))

#Exercice01

fruits_list = ["apple","banana","cherry"]

print(fruits_list)

print(fruits_list[2])

del (fruits_list[1])

fruits_list.append('orange')

print(f' list is {len(fruits_list)}')
num_list= [0, 16, 23, 93, 67, 5, 6, 7, 80, 98]

num_list.sort()

print(num_list)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[0:4])

list1 = [1,2,3] 
list2 = [4,5,6]
list3=list1+list2
print(list3) 

quote = ("i believe humankind that is fait of humanity")
print(len(quote))
print(quote[0],quote[-1])
print(quote[0:4])

greeting="Hello "

morning ="World"

combine= greeting+morning

print (combine)

uppercase_quote = quote.upper()

print(uppercase_quote)

count = quote.count("a")
print(count)

quote = quote.replace("humanity", "journey")

print (quote)

words = quote.split()
print(words)

start_with_the = quote.startswith("The")
print(start_with_the)

