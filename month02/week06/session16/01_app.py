menu="""please select one of the following options:
1.Add a new entry for today
2.Veiw all entries
3.exit

Your selection:"""
from database import add_entry, get_entries

welcome_message = "Wellcome to the Programing Diary!"
print(welcome_message)


user_input= input('menu:')

user_input= int(user_input)

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
        get_entries()
    else:
        print('Invailid selection. Please try again!')