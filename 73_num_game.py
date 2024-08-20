import random

def player_number_guessing_game():
    input("Think of a number between 1 and 100, and I'll try to guess it: ")

    low = 1
    high = 100
    attempts = 0

    while True:
        guess = random.randint(low, high)
        print(f"I guess {guess}.")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"I guessed your number in {attempts+1} attempts!")
            break

        attempts += 1

player_number_guessing_game()



