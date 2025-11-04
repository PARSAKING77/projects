import random

num = [random.randint(1, 6) for _ in range(2)]

i = input("Roll the dice? (y/n): ")

if i == 'y'or'Y':
    print(num)
elif i == 'n'or'N':
    print("Thanks for playing:)")
else:
    print("invalid choice!")

