entries = []

#1. add_entry гэдэг функц тодорхойлоод түүнийг - параметр авдаг болгох
#entry_content, entry_date
#энэхүү - кортентоор entry dictionary entries дотор хадгалдаг болгох
# энэхүү утгуудыг хадгалахдаа

def add_entry(entry_content, entry_date):
    entry = {
        'content': entry_content,
        'date': entry_date
    }
    entries.append(entry)

def get_entries():
    for entry in entries:
        print(f"Date: {entry['date']}\n Content: {entry['content']}\n\n")
        

    return entries