import random

number= input('guess number:')

number= int(number)

random=random.randrange(1,100)

print(random)

def guess_the_number():
    print("Wellcome to'Guess the Number'game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

secret_number = random.randit(1,100)
attents= 0
guess= 0
while guess != secret_number:
    guess = int(input("Enter your name"))
    attents +=1
    if guess <secret_number:
        print("Хэт бага байна!")
    elif guess>secret_number:
        print("Хэт их байна!")
    else:
        print(f"Congratulation!. {secret_number} in {attents} attents")
    
 
