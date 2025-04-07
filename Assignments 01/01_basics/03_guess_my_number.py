# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48
# solution 
import random

secret_number = random.randint(1, 10)
attempts =5   # Maximum 3 guesses allowed

print("I have selected a number between 1 and 10. Can you guess it? 🤔")

for i in range(attempts):
    try:
        guess = int(input(f"({attempts - i} attempts left)  Enter your guess: "))

        if guess < secret_number:
            print(" Too low! Try again. ")
        elif guess > secret_number:
            print(" Too high! Try again.")
        else:
            print(f"🎉 Correct! The number was {secret_number}. You guessed it! 🏆✨")
            break
    except ValueError:
        print("⚠️ Please enter a valid number! 🚫")

# If user fails all attempts
else:
    print(f"❌ Out of attempts! The correct number was {secret_number}.")