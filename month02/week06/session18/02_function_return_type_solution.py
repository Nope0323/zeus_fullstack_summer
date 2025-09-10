#Exercise01

def greet(name):
    print(f"Hello{name}!")
result = greet("Bob")

print(result) # Output: Hello, Bob! followed by None

#Exercise02

def multiply_numbers(a,b):
    return a*b
product = multiply_numbers(4, 6)
print(product)
#Exersise03
def concatenate_strings(str1,str2):
    return str1+""+str2

full_string = concatenate_strings("Hello", "World")
print(full_string)
#Exersise04
def is_even(number):
    return number % 2 == 0
print(is_even(4))
print(is_even(7))
# Output: True
# Output: False

#Exersise05

def get_max(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return a
    
    #Exercise06
def calculate_area_rectangle(legth,width):
    return legth * width


area = calculate_area_rectangle(5,8)
print(area)

#Exersice07 

def get_first_element(first):
    if  first:
        return first[0]
    return None

print(get_first_element([1, 2, 3]))  # Output: 1
print(get_first_element([]))

def power(base, exponent):
    return base ** exponent

print(power(2, 3))  # Output: 8 (2 * 2 * 2)
print(power(5, 2))  # Output: 25 (5 * 5)

def find_max_in_list(lst):
    if not lst:
        return None  
    max_val = lst[0]# 0 deer bga utgiiig max gej awah
    for item in lst[1:]:#item gej nerleed 1 deerees 0 oos busad toog tolno
        if item > max_val:#0 tei tentsuulj shalgaj bna
            max_val = item# 1 1 eern hartsuulaad ih toogoo max_val ruu hiinee
    return max_val # ih toogoo butsaana

print(find_max_in_list([3, 1, 4, 1, 5, 9]))  # Output: 9
print(find_max_in_list([]))                 # Output: None

#Exersice10
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

    # Solution Here
print(calculate_average([10, 20, 30]))
print(calculate_average([]))
# Output: 20.0
# Output: None