import random

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors."))
if user_choice >= 3 and user_choice < 0 :
    print("Invalid")
else:
    computer_choice = random.randint(0,2)
    print("computer chose: ")
    print(computer_choice)
    if user_choice < computer_choice:
        print("You lose.")
    elif computer_choice < user_choice:
        print("You win.")
    elif computer_choice == user_choice :
        print("It's draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")
    else:
        print("You win.")
