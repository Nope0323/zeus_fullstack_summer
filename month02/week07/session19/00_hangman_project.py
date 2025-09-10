import random

def get_word():
    '''Дараах list- ээс санамсаргүй үг буцаанав'''
    word = [
        "python", 
        "hangman", 
        "challenge",
        "programming",
        "developer",
        "function",
        "variable",
        "list",
        "dictionary",
        "tuple",
    ]
    return random.choice(word)

def display_word(word , guessed_letters):
    '''Үгнүүдийг харуулах'''
    displayed =""
    for letter in word:
        if letter in guessed_letters:
            displayed+= letter
        else:
            displayed+="_"
    return displayed.strip()


def hangman():
    word_to_guess = get_word()
    guessed_letters = []
    attempts = 6
    print("Тавтай морилно уу, Үг Таах Тоглоомд!")
    print("Үгийг таана уу. Та 6 оролдлоготой.")

   # for position in range (len(get_word)):
    #    letter = get_word[position]
     #   if letter == :
      #      display[position] = letter


    if __name__=="__main__":
        pass