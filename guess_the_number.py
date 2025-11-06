# Guess the Number Game
import random

print("Welcome to Mirrors199's Guess the Number Game!")

# Computer picks a random number between 1 and 20
number = random.randint(1, 20)

attempts = 0
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")

print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
