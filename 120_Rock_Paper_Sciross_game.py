import random

def get_computer_choice():
    choices = ['r', 'p', 's']
    return random.choice(choices)

def get_user_emoji(user_choice):
    if user_choice == 'r' or 'R':
        return 'Rock 🌎'
    elif user_choice == 'p' or 'P':
        return 'Paper 📄'
    elif user_choice == 's' or 'S':
        return 'Scissors ✂️'



def get_computer_emoji(choice):
    if choice == 'r':
        return 'Rock 🌎'
    elif choice == 'p':
        return 'Paper 📄'
    else:
        return 'Scissors ✂️'

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "DRAW!!!"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        return "YOU WWWWWWWWWWIIIIIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNN!!!!!!!!!!!!!!!!"
    else:
        return "YOU LOSE!!!"

while True:
    user_choice = input("Rock, Paper or Scissors (r/p/s): ")
    if user_choice not in ['r','R', 'P','p', 'S','s']:
        print("invalid choice!")
    else:
        computer_choice = get_computer_choice()
        print(f"YOU ({get_user_emoji(user_choice)})")
        print(f"COMPUTER ({get_computer_emoji(computer_choice)})")
        print(determine_winner(user_choice, computer_choice))
        break