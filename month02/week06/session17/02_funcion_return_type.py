def add_two_number(a,b):
    return a+b

print(add_two_number(5,6))
result_01 = add_two_number(5,3)
print(result_01)

def get_user_info():
    name="Alice"
    age=30
    return name, age
user_name, user_age = get_user_info()
print(f"Name: {user_name}, Age: {user_age}") # Output: Name: Alice, Age:30

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

#Exercise03

def concatenate_strings(a,b):
    return a+b

full_string = concatenate_strings("Hello", "World")
print(full_string)

#Exercise04

def is_even(number):
    return number % 2 == 0
# Solution Here
print(is_even(4))
print(is_even(7))
# Output: True
# Output: False

#Exercise05

def get_max(a,b):
    return a if a >b else b

print(get_max(10, 5))
print(get_max(3, 9))
# Output: 10
# Output: 9

#Exercise06
def calculate_area_rectangle(legth,width):
    return legth * width


area = calculate_area_rectangle(5,8)
print(area)

#Exersice07 

def get_first_element(first):
    if not first:
        return None
    return first[0]

print(get_first_element([1, 2, 3]))  # Output: 1
print(get_first_element([]))

def power(base, exponent):
    return base ** exponent

#Exersice08
# Test the function
print(power(2, 3))  # Output: 8 (2 * 2 * 2)
print(power(5, 2))  # Output: 25 (5 * 5)