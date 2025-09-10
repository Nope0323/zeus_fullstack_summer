import random
import string

letters = [
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z",
]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to PyPassword ")

password =""

nr_letters = int(input("How many letters would you like in you like in your password\n"))
nr_symbols = int(input("How many letters would you like in you like ?\n"))
nr_numbers = int(input("How many letters would you like in you like ?\n"))

for n in range(0,nr_letters):
    random_char = random.choice(letters)
    password+=random_char

for n in range(0,nr_symbols):
    random_char = random.choice(letters)
    password+=random_char

for n in range(0,nr_numbers):
    random_char = random.choice(numbers)
    password+=random_char

random.shuffle(password)
password_char="".join(password)
print(password_char)
