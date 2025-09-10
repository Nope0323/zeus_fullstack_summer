menu="""please select one of the following options:
1.Add a new entry for today
2.Veiw all entries
3.exit

Your selection:"""
from database_sqlite import add_entry, get_entries, create_table

welcome_message = "Wellcome to the Programing Diary!"
print(welcome_message)

create_table()

#while   user_input  !='3':
#    user_input = input(menu)
#walrus operator
while (user_input:=input(menu)) !="3":
    if user_input=="1":
        print("Adding...")
        
        entry_content= input("Enter the content: ")
        entry_date = input("Enter the date (YYYY-MM-DD): ")
        add_entry(entry_content,entry_date)
        
    elif user_input=="2":
        print("Viewing")
        entries =get_entries()
        for entry in entries:
            print(f"{entry['date']}\n{entry['content']}\n\n")
        get_entries()
    else:
        print('Invailid selection. Please try again!')