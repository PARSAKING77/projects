import random

def guess_number():
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it.")
    
    while True:
        guess = int()
        attempts += 1
        
        if guess < secret_number:
            print("low! try again")
        elif guess > secret_number:
            print("high! try again")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_number()