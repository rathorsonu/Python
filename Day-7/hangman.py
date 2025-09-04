import random

Word_list = ["ardvark", "baboon", "camel"]

#TODO-1. Randomly choose a word from the word_list and assign it to a variable called chosen_word.
lives = 6
choose_word = random.choice(Word_list)
print(f"the chosen word is {choose_word}")

#create a placeholder with the same number of letters as the chosen word
placeholder = ""
word_length  = len(choose_word)

for position in range(word_length):
    placeholder += " _ "
print(placeholder)

#TODO-2. Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
game_ower = False
corrected_letters = []

while not game_ower:
    guess = input("Guess a Letter: ").lower()
    #TODO-3. Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    dispaly_value = ""

    for letter in choose_word:
        if letter == guess:
            dispaly_value += letter
            corrected_letters.append(letter)
        elif letter in corrected_letters:
            dispaly_value += letter
        else:
            dispaly_value += " _ "
    print(dispaly_value)

    if guess not in choose_word:
        lives -= 1
        print(f"you have {lives} lives left")
        if lives == 0:
            game_ower = True
            print("You Lose")

    if " _ " not in dispaly_value:
        game_ower = True
        print("You Win")

