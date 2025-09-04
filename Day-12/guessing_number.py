import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

input_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
chosen_number = random.randint(1,100)
guess = 0

def set_difficulty(level):
    if input_level == 'easy':
        total_attempts = 10
    else:
        total_attempts = 5
    return total_attempts

attempts_remaining = set_difficulty(level=input_level)


def check_answer(guess, chosen_number, attempts):
    if guess > chosen_number:
        print("Too high.")
        return attempts - 1
    elif guess < chosen_number:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {chosen_number}.")        
        
while guess != chosen_number and attempts_remaining > 0:
    print(f"You have {attempts_remaining} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts_remaining = check_answer(guess, chosen_number, attempts_remaining)
    if attempts_remaining == 0:
        print("You've run out of guesses, you lose.")
        print(f"The correct number was {chosen_number}.")
    elif guess != chosen_number:
        print("Guess again.")
