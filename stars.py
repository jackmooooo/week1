def directory(which):
    if which == "first":
        one(int(input("ammount >>")))
    elif which == "second":
        two(int(input("ammount >>")))
    elif which == "third":
        three(int(input("ammount of waves >>")), int(input("size of wave >>")))
    elif which == "fourth":
        four(int(input("base width >>")))


def one(ammount):
    string = ""
    for i in range(ammount):
        string += "*"
        print(string)

def two(ammount):
    string = "*"*ammount
    for i in range(ammount):
        string = string[:-1]
        print(string)

def three(ammount, maxWidth):
    waves = ammount*maxWidth
    string = ""
    direction = 0
    for i in range(waves):
        if len(string) == maxWidth:
            direction = 1
        elif len(string) == 1:
            direction = 0
        if direction == 0:
            string += "*"
            print(string)
        elif direction == 1:
            string = string[:-1]
            print(string)
"""
def four(length):
    pyramid = ""
    if
    for i in range(length):
            pyramid += " "*(length
"""
def five():

directory(input("what pattern? >>"))
