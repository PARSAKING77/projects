import random

user = int(input("Please select one of thees options: (1): Rock🪨 (2): Paper📄 (3): Scissors✂️ "))
bot = random.choice([1, 2, 3])

if user == bot:
    print("You selected: ", user, "and the bot selected: ", bot, "It's a tie!")
elif user == 1 and bot == 2:
    print("You selected: ", user, "and the bot selected: ", bot, "You lose!")
elif user == 1 and bot == 3:
    print("You selected: ", user, "and the bot selected: ", bot, "You win!")
elif user == 2 and bot == 1:
    print("You selected: ", user, "and the bot selected: ", bot, "You win!")
elif user == 2 and bot == 3:
    print("You selected: ", user, "and the bot selected: ", bot, "You lose!")
elif user == 3 and bot == 1:
    print("You selected: ", user, "and the bot selected: ", bot, "You lose!")
elif user == 3 and bot == 2:
    print("You selected: ", user, "and the bot selected: ", bot, "You win!")
else:
    print("Invalid input! Please enter 1, 2, or 3.")