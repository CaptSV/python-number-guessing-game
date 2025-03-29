# Number Guessing Game:
# Generate a random number within a certain range.
# Prompt the user to guess the number.
# Provide feedback (too high, too low, correct).
# Keep track of the number of attempts.
# Skills: Random number generation (random module), user input (input()), conditional statements (if/elif/else), loops (while).
# Example: The computer picks a number between 1 and 100. You have to guess it in as few tries as possible.

import random

not_number = False
continue_check = True
player_tries = 3

print("Guess the number!\nSelect a number between 1 to 20.\nYou have 3 tries!")

while continue_check:
    random_number = random.randrange(1, 20)

    while player_tries > 0:
        guess = input("Enter a number: ")
        guess = int(guess)

        if guess < 1 or guess > 20:
            print("Invalid Guess!")
        elif guess < random_number:
            print("Too Low")
            player_tries -= 1
        elif guess > random_number:
            print("Too High")
            player_tries -= 1
        else:
            print(f"That's correct! The number is {random_number}")
            break
    print(f"The correct answer is {random_number}")

    continue_answer = input("Do you want to try again? (Y/N): ")
    if continue_answer.upper() == "N":
        continue_check = False
    else:
        player_tries = 3
        continue