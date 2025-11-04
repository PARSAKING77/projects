import random

def color_guess():
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "black", "white","brown", "pink", "gray", "silver","gold","crimson","bronze"]
    color_to_guess = random.choice(colors)
    guess = None
    while guess != color_to_guess:
        guess = input("pick your color: ")
        if guess != color_to_guess:
            print("your color is incorrect. try again.: ")
    print("WWWWWWWWWWWWOOOOOOOOOOOOOOOOOOOOOOOOOOWWWWWWWWWWWWWWWWWWWWW!!!!!!!!!!!!!!!!!!!!!! YOUR COLOR IS CORRECT!!!!!!!!!!!!!!!!!!")

color_guess()