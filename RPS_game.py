import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = int(input("What do you want to choose? 0 for Rock, 1 for Paper, and 2 for Scissors: "))

if user_choice == 0:
    print("Your choice:\n", Rock)
elif user_choice == 1:
    print("Your choice:\n", Paper)
elif user_choice == 2:
    print("Your choice:\n", Scissors)
else:
    print("Your choice is not valid")

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print("Computer choice:\n", Rock)
elif computer_choice == 1:
    print("Computer choice:\n", Paper)
elif computer_choice == 2:
    print("Computer choice:\n", Scissors)

if user_choice == computer_choice:
    print("It's a tie! 😐")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (
        user_choice == 2 and computer_choice == 1):
    print("You win! 🎉")
else:
    print("You lose! 😔")
