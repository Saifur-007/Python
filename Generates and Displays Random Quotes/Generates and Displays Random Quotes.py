# This program uses the random module to select a quote from a list of quotes and displays it. The if __name__ == "__main__": line is a Python idiom that allows the program to be run as a standalone script. When the script is run, it will print a random quote to the console.




import random

quotes = [    "Success is not final, failure is not fatal: it is the courage to continue that counts.",    "Don't watch the clock; do what it does. Keep going.",    "The best way to predict the future is to create it.",    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",    "Successful and unsuccessful people do not vary greatly in their abilities. They vary in their desires to reach their potential."]

def display_quote():
    quote = random.choice(quotes)
    print("\nHere's a quote to inspire you:")
    print(f"\t{quote}")

if __name__ == "__main__":
    display_quote()
