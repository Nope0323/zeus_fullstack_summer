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

def most_frequent_char(text):
    """Текст доторх хамгийн олон давтагдсан тэмдэгтийг олно."""
    counts = {}
    # TODO
    for n in text:
        counts[n] = counts.get(n,0) + 1 # {"п":1, "р":2}


    most_frequent = None #k
    max_count = -1 #v
    # TODO
    for k, v in counts.items():
        if v > max_count:
            most_frequent = k
            max_count = v
    return most_frequent, max_count

    
my_text = "програмчлалын үндсэн ойлголтууд"
print(f"Хамгийн олон орсон тэмдэгт: '{most_frequent_char(my_text)}'")

def add_contact(book, name, phone):
    """Утасны дэвтэрт шинэ контакт нэмнэ."""
# TODO
def find_contact(book, name):
    """Нэрээр нь контакт хайж, олдвол мэдээллийг буцаана."""
# TODO
# Утасны дэвтэр (толь бичгийн жагсаалт)
contact_book = []
add_contact(contact_book, "Болд", "9911XXXX")
add_contact(contact_book, "Сарнай", "9988XXXX")
found = find_contact(contact_book, "Сарнай")
if found:
    print(f"Олдсон: {found}")
else:
    print("Контакт олдсонгүй.")