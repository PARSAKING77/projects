import os
os.system("")


class style():
  RESET = '\033[0m'
  RED = '\033[31m'
  GREEN = '\033[32m'


score = 0


Question1 = ["Question 1:","What is the capital of France?"]
print(Question1)

answer1 = ["Berlin", "Madrid", "Paris", "Rome"]
for x, answer1 in enumerate(answer1, start=65):  
    print(chr(x) + ". " + answer1)

user1 = input("Your answer: ")


if user1 == 'C':
    print(style.GREEN + "{0}".format("CORRCET!!!") + style.RESET)
    score += 1  
    
elif user1 == 'A' or 'B' or 'D':
    corr1 = 'C'
    print(style.RED + "{0}".format(f"WRONG!!! The correct answer is {corr1}") + style.RESET)



Question2 = [' which planet is kknown as the red planet?']
print(Question2)

answer2 = ["Earth", "Mars", "Jupiter", "Saturn"]
for x, answer2 in enumerate(answer2, start=65):  
    print(chr(x) + ". " + answer2)

user2 = input("Your answer: ")

if user2 == 'B':
    print(style.GREEN + "{0}".format("CORRCET!!!") + style.RESET)
    score += 1  
    
elif user2 == 'A' or 'C' or 'D':
    corr2 = 'B'
    print(style.RED + "{0}".format(f"WRONG!!! The correct answer is {corr2}") + style.RESET)




Question3 = ['What is the largest ocean on Earth?']
print(Question3)

answer2 = ["Atlantic", "Indian", "Arctic", "Pacific"]
for x, answer2 in enumerate(answer2, start=65):  
    print(chr(x) + ". " + answer2)

user3 = input("Your answer: ")

if user3 == 'D':
    print(style.GREEN + "{0}".format("CORRCET!!!") + style.RESET)
    score += 1  

elif user3 == 'A' or 'C' or 'B':
    corr3 = 'D'
    print(style.RED + "{0}".format(f"WRONG!!! The correct answer is {corr3}") + style.RESET)


if score == 3:
    print("Quiz over! Your score is 3 of 3")
elif score == 2:
    print("Quiz over! Your score is 2 of 3")
elif score == 1:
    print("Quiz over! Your score is 1 of 3")
else:
    print("Quiz over! Your score is 0 of 3")
