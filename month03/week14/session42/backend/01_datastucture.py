#ex01
def filter_even_numbers(number_list):
    """Жагсаалтаас тэгш тоонуудыг шүүж, шинэ жагсаалт буцаана."""
    # ev_numbers = []
    # for n in number_list:
    #     if n % 2 == 0:
    #         ev_numbers.append(n)
    # return ev_numbers
    return [n for n in number_list if n%2==0]

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter_even_numbers(my_numbers)
print(f"Анхны жагсаалт: {my_numbers}")
print(f"Шүүсэн жагсаалт: {evens}")

#ex02
def find_common_elements(list1, list2):
    """Хоёр жагсаалтын ерөнхий элементүүдийг олж буцаана."""
    common_elements = []
    # TODO
    for m in list1:
        if m in list2:
            common_elements.append(m)
    return common_elements

list_a = [1, 2, 3, 4, 5, "алим"]
list_b = [4, 5, 6, 7, 8, "алим"]
commons = find_common_elements(list_a, list_b)
print(f"Ерөнхий элементүүд: {commons}")

#ex03
def word_length_dict(word_list):
    """Үгсийн жагсаалтыг {үг: урт} гэсэн толь бичиг болгоно."""
    result_dict = {}
    # TODO
    for n in word_list:
        
        result_dict[n]=len(n)
    return result_dict
words = ["python", "програм", "өгөгдөл", "бүтэц"]
lengths = word_length_dict(words)
print(lengths)

#ex04
def get_grade_status(scores_dict):
    """Дүнгийн толь бичгийг статусын толь бичиг болгоно."""
    status_dict = {}

    # TODO
    for m, n in scores_dict.items():

        if  n >= 60:
            status_dict[m]="тэнцсэн"

        else :
            status_dict[m]="тэнцээгүй"
            
    return status_dict

scores = {"Болд": 85, "Сарнай": 92, "Дорж": 58, "Нараа": 77}
statuses = get_grade_status(scores)
print(statuses)

#ex05
def merge_dicts(dict1, dict2):
    """Хоёр толь бичгийг нэгтгэнэ."""
    merged = dict1.copy() # dict1-ийн хуулбарыг үүсгэх
    for k,v in dict2.items():
        merged[k] = v
    return merged

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 20, 'd': 40}
result = merge_dicts(d1, d2)
print(f"Нэгтгэсэн толь бичиг: {result}")

def most_frequent_char(text):
    """Текст доторх хамгийн олон давтагдсан тэмдэгтийг олно."""
    counts = {}
    # TODO
    most_frequent = None
    max_count = -1
    # TODO
my_text = "програмчлалын үндсэн ойлголтууд"
print(f"Хамгийн олон орсон тэмдэгт: '{most_frequent_char(my_text)}'")