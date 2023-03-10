print("Welcome to Random Quote Generator.")

import random

quotes = [    "Success is not final, failure is not fatal: it is the courage to continue that counts.",    "Believe you can and you're halfway there.",    "The only way to do great work is to love what you do.",    "Don't watch the clock; do what it does. Keep going.",    "The best way to find yourself is to lose yourself in the service of others.",    "The only limit to our realization of tomorrow will be our doubts of today."]

def get_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    print(get_quote())