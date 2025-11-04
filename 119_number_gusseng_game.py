import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
    except ValueError:
        print("ERROR: Please eneter a valid number!")
        continue

    if guess == number_to_guess:
        print("YOU WWWWWWWWIIIIIIIIIIIIIIIIIINNNNNNNNNNN!!!!!!!!!!!!")
        break
    elif guess > number_to_guess:
        print("TOO HIGH!")
    else:
        print("TOO LOW!")