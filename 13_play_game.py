import random

def choose_word():
   words = ["tiger" ,"toad" ,"trout", "turkey" ,"turtle" ,"weasel" ,"whale"
             ,"wolf", "wombat" ,"zebra", "cat" ,"dog", "phone","playstation",
               "rubick", "car","ea","ubisoft","laptop","mouse","glass","face",
               "robot","game","youtuber","youtube","ball","apple","house","money",
               "keyboard","notebook","marker","pencile","eraser","pants","tshert","book",
               "shose","socks","nose","mouth","flower","ice","ice creame","burger","pizza",
               "food","fast","fast food","familiy","egg","head","suit","sheep","dinesore",
               "microphone","camera","painting","sister","brother","dad","mom","table","stinkey",
               "delete","acount","wallet","color","pink","black","gameing","green","purpule","canada",
               "iran","rock","germany","teacher","student","japan","sick","anime","beach","orenge","blue",
               "blueberry","logo","strawberry","camel","pineappele","spongbob","patric","fish","fitnes","finger",
               "story","idea","usa","norway","pakistan","afghanstan","uzbakistan","asia","china","south korea","greec",
               "italy","monoco","turckye","spain","france","yemen","egupt","iraq","indonesia","fiji","samoa","belgiume",
               "mexico","slovonia","plastine","israel","nort korea","russia","ping pong","tenis","meme","girl","lamborghini",
               "ferari","buggati","pasta","vegetables","sibling","mario","luoigi","song","selfie","hair","eye","messi","ronaldo",
               "mbape","search","kurdistan","linux","windows","door","store","bottel","calaender","mute","network","homework",
               "pain","python","html","css","c++","go","charge","batery","rap","pop","kpop","call","chat","parking","key","lock",
               "unlock","clock","calculator","end","dragon","number","control","break","strng","istagram","real","neymar","pepe",
               "wiif","holder","cabin","baby","boss","sleep","low","high","king","qeen","letter","lamp","television","math",
               "gold","iron","diamond","welcome","join","bubel","internet","brazil","argantina","africa","yello","male","femail",
               "mail","random","name","stadium","spanish","japnis","bordcast","last","grass","correct","incorrect","oil","shaft",
               "tin","sweet","index","opinion","land","hear","due","option","chase","pound","sesitive","flawed","agree","output",
               "result","rub","yard","experience","terminal","angel","sheet","bold","module","budge","toll","detail","transform",
               "bag","suspect","beginning","soap","treat","aroww","rage","clothes","scan","trap","drink","official","jury","lemon",
               "director","lie","prize","law","ask","tick","trend","job","manual","base","trait","fuel","ant","prcess","grant","call",
               "border","bring","rate","anger","doller","adderes","engain","sleep","local","mentor","edition","donkey","haaland",
               "salah","nonez","vandijk","taremi","jahanbakhsh","beyranvand","bekham","grilish","mane","vini","blingham","walker",
               "dimaria","bleses"]
   return random.choice(words)

def play_game():
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 15
    guessed_word = ["_"] * len(word_to_guess)
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