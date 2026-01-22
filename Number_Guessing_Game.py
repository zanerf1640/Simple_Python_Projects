"""
This is a simple number guessing game implemented in Python.
This is to help understand the concept of Binary Seearch adn Algorithm efficiency.
The player has to guess a randomly generated number between 1 and 100.

Author: Zane Francis
"""
import random
 
def number_guessing_game():
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed:
        try:
            user_guest = int(input("Enter your guess: "))
            attempts += 1
            if user_guest < 1 or user_guest > 100:
                print("Number out of range! Please select a number between 1 and 100.")
                continue
            if user_guest < number_to_guess:
                print("Too low! Try again.")
            elif user_guest > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a valid integer between 1 and 100.")

if __name__ == "__main__":
    number_guessing_game()