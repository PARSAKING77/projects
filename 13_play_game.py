import random

def choose_word():
   words = ["apple", "banana", "orange", "grape", "strawberry","lamborghini",
   "car","motorcycel","benz","bmw","fotball","volyball","purpul","red",
   "pink","black","white","baketball","ball","king","queen","laptop",
   "pc","art","light","work","HTML","javascript","python","css","code",
   "codeing","mouse","keyboard","display","xbox","playstation","dualsens",
   "dualshocke","charge","robot","table","dor","click","toilet","freand",
   "father","mother","sister","brother","sheep","dog","cat","horse","red dead"
   ,"gta","fifa","mincraft","google","nose","ears","eye","turtule","wolf","key","wc",
   ]
   return random.choice(words)

def play_game():
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 20
    guessed_word = ["_"] * len(word_to_guess)
    
    print("Welcome to the Name Guessing Game!")
    print("The word has {} letters. You have {} attempts.".format(len(word_to_guess), attempts))
    
    while attempts > 0 and "_" in guessed_word:
        print(" ".join(guessed_word))
        guess = input("Enter a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print("Correct guess!")
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
        else:
            print("Incorrect guess!")
            attempts -= 1
        
        print("You have {} attempts left.".format(attempts))
    
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word: {}".format(word_to_guess))
    else:
        print("Sorry, you ran out of attempts. The word was: {}".format(word_to_guess))

play_game()