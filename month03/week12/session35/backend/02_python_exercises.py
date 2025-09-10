# Функцийг дуудах

def add_numbers(a,d):
    result=a+d
    return result
result = add_numbers(10, 5)
print(f"Хоёр тооны нийлбэр: {result}")

#ex02

my_list = [1, 9, 3, 22, 15]

def find_max(my_list):
    return max(my_list)


max_value = find_max(my_list)
print(f"Жагсаалтын хамгийн их утга: {max_value}")

#ex03

def get_string_length(text):
    return len("".join(text))
length = get_string_length("Сайн байна уу?")
print(f"Тэмдэгт мөрийн урт: {length}")

#ex04
original_list = [1, 2, 3, 4, 5, 6, 7, 8]
def filter_even_numbers(original_list):
    even_numbers = []
    for number in original_list:
        if number %2==0:
            even_numbers.append(number)

    return even_numbers 
evens = filter_even_numbers(original_list)
print(f"Тэгш тоонууд: {evens}")

#ex05
