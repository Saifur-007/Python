
# Python program that generates a random number between 1 and 10 and then prompts the user to guess the number




import random

number = random.randint(1, 10)
guess = int(input("Guess the number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed the number!")
else:
    print("Sorry, the number was " + str(number) + ". Try again!")
