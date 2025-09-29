def filter_even_numbers(number_list):
    """Жагсаалтаас тэгш тоонуудыг шүүж, шинэ жагсаалт буцаана."""
    # TODO
    ev_numbers = []
    for n in number_list:
        if n % 2 ==0:
            ev_numbers.append(n)
    return ev_numbers
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter_even_numbers(my_numbers)
print(f"Анхны жагсаалт: {my_numbers}")
print(f"Шүүсэн жагсаалт: {evens}")

def find_common_elements(list1, list2):
    """Хоёр жагсаалтын ерөнхий элементүүдийг олж буцаана."""
    common_elements = []
    # TODO
    for n in list1:
        if n in list2:
            common_elements.append(n)
    return common_elements

list_a = [1, 2, 3, 4, 5, "алим"]
list_b = [4, 5, 6, 7, 8, "алим"]
commons = find_common_elements(list_a, list_b)
print(f"Ерөнхий элементүүд: {commons}")