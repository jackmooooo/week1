import random
print("Welcome to hangman!")
def directory(response):
    if response == "easy":
        easy()
    if response == "special cookie":
        special()
    if response == "medium":
        medium()
    if response == "hard":
        hard()
words = ["cat", "dog", "cow", "fish", "pig", "anaconda", "the", "banana", "pizza", "basket ball", "at", "an", "a", "cupcake", "sun", "mouse", "fire", "house", "banjo", "fiddle", "apple", "orange", "yellow", "yote", "yeet", "teeth", "minecraft"]
def easy():
    correct = words[random.randint(0, len(words)-1)]
    word = ("_"*len(correct))
    hp = 6
    while hp >= 0:
        if word.count("_") == 0:
            win()
            if input("would you like to restart?  >> ") == "yes":
                directory(input("easy/medium/hard  >> "))
            else:
                return
        if hp == 6:
            safe(word)
        elif hp == 5:
            head(word)
        elif hp == 4:
            torso(word)
        elif hp == 3:
            onearm(word)
        elif hp == 2:
            noleg(word)
        elif hp == 1:
            lastleg(word)
        elif hp == 0:
            dead()
            if input("would you like to restart?  >> ") == "yes":
                directory(input("easy/medium/hard  >> "))
            else:
                return
        include = input("what letter?  >> ")
        if correct.count(include) == 0 or word.count(include) > 0:
            hp = hp-1
            print("you have "+str(hp)+" misses left")
        else:
            new = list(word)
            for i in range(len(correct)):
                if correct[i] == include:
                    new[i] = include
            word = ''.join(new)
def medium():
    correct = words[random.randint(0, len(words)-1)]
    word = ("_"*len(correct))
    hp = 4
    while hp >= 0:
        if word.count("_") == 0:
            win()
            if input("would you like to restart?  >> ") == "yes":
                directory(input("easy/medium/hard  >> "))
            else:
                return
        if hp == 4:
            safe(word)
        elif hp == 3:
            head(word)
        elif hp == 2:
            torso(word)
        elif hp == 1:
            noleg(word)
        elif hp == 0:
            dead()
            if input("would you like to restart?  >> ") == "yes":
                directory(input("easy/medium/hard  >> "))
            else:
                return
        include = input("what letter?  >> ")
        if correct.count(include) == 0 or word.count(include) > 0:
            hp = hp-1
            print("you have "+str(hp)+" misses left")
        else:
            new = list(word)
            for i in range(len(correct)):
                if correct[i] == include:
                    new[i] = include
            word = ''.join(new)
def hard():
    correct = words[random.randint(0, len(words)-1)]
    word = ("_"*len(correct))
    hp = 3
    while hp >= 0:
        if word.count("_") == 0:
            win()
            if input("would you like to restart?  >> ") == "yes":
                directory(input("easy/medium/hard  >> "))
            else:
                return
        if hp == 3:
            safe(word)
        elif hp == 2:
            torso(word)
        elif hp == 1:
            noleg(word)
        elif hp == 0:
            dead()
            if input("would you like to restart?  >> ") == "yes":
                directory(input("easy/medium/hard  >> "))
            else:
                return
        include = input("what letter?  >> ")
        if correct.count(include) == 0 or word.count(include) > 0:
            hp = hp-1
            print("you have "+str(hp)+" misses left")
        else:
            new = list(word)
            for i in range(len(correct)):
                if correct[i] == include:
                    new[i] = include
            word = ''.join(new)
def special():
    print("you're a special cookie!")
    print("")
    print("    _______________")
    print("    |         *   |")
    print("    |     *       | ")
    print("    |   *     *   |")
    print("    |     *       |")
    print("    |   *    *    |")
    print("    |_____________|")

def dead():
    print(" ________")
    print(" |      |")
    print(" |      O")
    print(" |     /|\ ")
    print(" |    * | *")
    print(" |     / \ ")
    print("/ \ ")
    print("")
    print("you have died")
def lastleg(word):
    print(" ________")
    print(" |      |")
    print(" |      O")
    print(" |     /|\ ")
    print(" |    * | *")
    print(" |     / ")
    print("/ \ ")
    print("")
    print(word)
def noleg(word):
        print(" ________")
        print(" |      |")
        print(" |      O")
        print(" |     /|\ ")
        print(" |    * | *")
        print(" |")
        print("/ \ ")
        print("")
        print(word)
def onearm(word):
        print(" ________")
        print(" |      |")
        print(" |      O")
        print(" |     /|")
        print(" |    * |")
        print(" |")
        print("/ \ ")
        print("")
        print(word)
def torso(word):
        print(" ________")
        print(" |      |")
        print(" |      O")
        print(" |      |")
        print(" |      |")
        print(" |")
        print("/ \ ")
        print("")
        print(word)
def head(word):
        print(" ________")
        print(" |      |")
        print(" |      O")
        print(" |")
        print(" |")
        print(" |")
        print("/ \ ")
        print("")
        print(word)
def safe(word):
        print(" ________")
        print(" |      |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("/ \ ")
        print("")
        print(word)
def win():
    print(" you win !!!!!")
    print("_______________________________________")
    print("| *       *       +      *       *    |")
    print("|  \     /      /  \      \     /     |")
    print("|   \   /      /    \      \   /      |")
    print("|     +       /      \       +        |")
    print("|     I      /________\      I        |")
    print("|     I     /          \     I        |")
    print("|     I    /            \    I        |")
    print("|     I   /              \   I        |")
    print("|_____________________________________|")



directory(input("easy/medium/hard  >> "))
