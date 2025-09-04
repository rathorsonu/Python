import random
user_choice = int(input("What do you choose? Type 0 for Rock 1 for paper or 2 for scisors:\n"))
print(f"user choice is {user_choice}")

computer_choice = random.randint(0,2)
print(f"computer choice is {computer_choice}")

if user_choice >=3 or user_choice <0:
    print("you type invalid input")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice ==0  and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win")
elif user_choice == computer_choice:
    print("It is a draw")
else:
    print("you type invalid input")

