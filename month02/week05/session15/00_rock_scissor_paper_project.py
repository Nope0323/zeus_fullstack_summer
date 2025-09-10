import random
"""Rock, Paper, Scissors Game Question."""

# Дараах төсөл нь компьютер болон таны хооронд хайч, чулуу, цаас гэдэг тоглоом тоглох юм.
# Хайч нь цаасыг ялна
# Цаас нь чулууг ялна
# Чулуу нь хайчийг ялна.
# Компьютер хэрэглэгчээс сонголтыг асуух бөгөөд хэрэглэгч 0, 1 эсвэл 2-ын тооны нэгийг сонгоно.
# Хэрвээ компьютер ялвал "You lose!"
# Хэрвээ тоглогч ялвал "You win!"
# Хэрвээ тоглогч буруу тоо оруулвал "You typed an invalid number. You lose."
# Хэрвээ тоглогч болон компьютер адилхан сонговол "It's a draw"
# гэж хэвлэнэ.
# Тэгээд хэрэглэгч болон компьютерын сонгосон тооны дагуу list-нээс index-ээр нь сонгож
# дүрсүүдийг харуулаад хэн нь хожсон эсвэл тэнцсэн эсэхийг харуулаад тоглоом дуусна.
# Хэрэглэгчээс гарнаас утга авахдаа дараах асуултыг асууна.
# "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


game_images = [rock, paper, scissors]

human_choice= input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ")
human_choice= int(human_choice)
computer_choice= random.randint(0,2)

print(game_images[human_choice])
if human_choice <computer_choice: #0,2
    print(f"Computer choice{game_images[computer_choice]}")
    print("You win!")
elif human_choice==computer_choice:#0=0
    print(f"Computer choice{game_images[computer_choice]}")
    print("You draw")
elif human_choice > computer_choice:#0=1
    print(f"Computer choice{game_images[computer_choice]}")
    print("You lost")
else:
    
    print("You typed an invalid number. You lose!")