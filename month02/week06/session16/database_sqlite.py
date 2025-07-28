import sqlite3

connection = sqlite3.connect('diary.db')

def create_table():
    with connection:
        connection.execute('Create table if not exists entries  (content Text, date TEXT);')
#1. add_entry гэдэг функц тодорхойлоод түүнийг - параметр авдаг болгох
#entry_content, entry_date
#энэхүү - кортентоор entry dictionary entries дотор хадгалдаг болгох
# энэхүү утгуудыг хадгалахдаа

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            'INSERT INTO entries (content,date )VALUES(?,?);',
            (entry_content,entry_date));
def get_entries():
    pass

