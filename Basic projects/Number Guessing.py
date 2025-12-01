# 🎯 Number Guessing Game
# This program lets the user guess a number chosen by the computer

import random  # Import the random module to generate random numbers

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

# The computer picks a random number between 1 and 100
secret_number = random.randint(1, 100)

# To keep track of how many guesses the user makes
attempts = 0

# Loop until the correct number is guessed
while True:
    # Ask the user for their guess
    guess = int(input("Enter your guess: "))
    attempts += 1  # Add one to the attempt counter

    # Check if the guess is correct, too low, or too high
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break  # End the loop when the user is correct
