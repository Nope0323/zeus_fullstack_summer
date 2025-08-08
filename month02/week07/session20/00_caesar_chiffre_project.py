Menu="""
1."encrypt" (шифрлэх)
2."decrypt" (тайлах)

Your selection:
"""

welcome_message = "Цезарийн шифр програмд тавтай морил!"
print(welcome_message)

code= input('code:')
code = int(code)

def caesar_cipher(text, key,direction):
    if direction=='decrypt':
        key*=-1
    result=''

    for char in text:
        if char.isalpha():
            pass
