import random, os, time, sys


def typeslow(str):
    global write
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n") 

def randomword():
    global words
    global word
    global hiddenword
    global guessed
    global lines    
    words = ["privilege", "quaint", "cross", "defend", "represent", "fool", "criminal", "refuse", "active", "paragraph", "crutch", "ankle", "survival", "volume", "retirement", "close", "shareholder", "first", "winner", "separation"]
    word = random.choice(words)
    hiddenword = list(word)
    guessed = []
    lines = []
    for i in range(len(hiddenword)):
        lines.append("_")

def hangman(attempts):
    
    global startattempts
    attempts = startattempts
    randomword()
    while attempts > 0:
        print(" ".join(lines))
        time.sleep(0.1)
        print("Already guessed letters: ", (", ".join(guessed)))
        time.sleep(0.1)
        print("Attempts left: ", attempts)
        time.sleep(0.1)
        print("Take a guess")
        time.sleep(0.1)        
        guess = input("> ")
        if hiddenword.count(guess) > 0:
            while hiddenword.count(guess) > 0:
                index = hiddenword.index(guess)
                lines.pop(index)
                hiddenword.pop(index)
                hiddenword.insert(index, "_")
                lines.insert(index, guess)
            guessed.append(guess) 
            os.system("cls")
        elif guess == " ":
            os.system("cls")
        elif guess == word:
            win()
        elif len(guess) != 1:
            os.system("cls")
            print("There were too many letters, go one by one")
        elif guessed.count(guess) > 0:
            os.system("cls")
            print("You already guessed this, try again")
        else:
            os.system("cls")
            guessed.append(guess)
            attempts = attempts-1
            print("That is not a letter in the word")
        if hiddenword.count("_") == len(hiddenword):
            win()
    
    os.system("cls")
    print("You ran out of attempts, you lose")
    print("The word was ", word)
    print("Do you want to try again? (Y/N)")
    if input("> ").lower().startswith("y"):
        os.system("cls")
        print("Would you like more guesses next time? (Y/N)")
        if input("> ").lower().startswith("y"):
            os.system("cls")
            print("Alright then, you'll get 3 more attempts this time")
            startattempts = startattempts+3
            hangman(startattempts)
            print("Loading")
            time.sleep(5)
            os.system("cls")
        else:
            print("Loading")
            time.sleep(5)
            os.system("cls")
            hangman(startattempts)
    else:
        os.system("cls")
        print("alrigh then, bye")

def win():
    os.system("cls")
    print(" ".join(lines))
    print("The word was ", word)
    print("You win, I guess")
    print("Wanna try again?")
    if input("> ").lower().startswith("y"):
        print("Loading")
        time.sleep(5)
        os.system("cls")
        hangman(startattempts)
    else:
        os.system("cls")
        print("Okay then, bye")
    

startattempts = 7

hangman(7)