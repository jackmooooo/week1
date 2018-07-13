"""
its not completely complete.
"""
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mult(a, b):
    c = 0
    for i in range(b):
        if c == 0:
            c = a
        else:
            c = add(c, a)
    return c
def div(a, b):
    return a/b
def pwr(a, b):
    c = 0
    for i in range(b):
        if c == 0:
            c = a
        else:
            c = mult(c, b)
    return c
def remain(a, b):
    c = div(a, b)
    d = int(c)
    e = sub(c, d)
    f = mult(e, b)
    return f
def bintodec(a):
    b = a.split('.')
    c = 0
    d = 0
    for i in range(len(b)):
        for x in range(len(b[i])):
            if i == 0:
                c += int(b[i][x])*(2**(len(b[i])-add(x, 1)))
            else:
                d += int(b[i][x])*(2**(x-len(b[i])))
    return add(c, d)
"""
def bintoOct(a):
    c = ""
    d = ""
    b = a.split(".")
    print(b)
    b[1] = add(str(b[1]), str(mult("0", int(remain(len(b[1])+1, 3)))))
    b[0] = add(str(mult("0", int(remain(len(b[0])+1, 3)))), str(b[0]))
    print(b)
    x = 0
    while x <= len(b[0])+1:
        print(c)
        c += str(bintodec(b[0][x:x-3]))
        x = x-3
    print(x)
    x = 0
    while x <= len(b[1]):
        print(d)
        d += str(bintodec(b[1][x:x+3]))
        x += 3
    print(x)
    print(c)
    print(d)
    return add(c, '.'+d)
"""
def helper(operation):
    if operation == 'add':
        print(add(float(input("number >>")), float(input("number >>"))))
    elif operation == 'sub':
        print(sub(float(input("number >>")), float(input("number >>"))))
    elif operation == 'mult':
        print(mult(int(input("number >>")), int(input("number >>"))))
    elif operation == 'div':
        print(div(float(input("number >>")), float(input("number >>"))))
    elif operation == 'pwr':
        print(pwr(int(input("number >>")), int(input("number >>"))))
    elif operation == 'remain':
        print(remain(int(input("number >>")), int(input("number >>"))))
    elif operation == 'bintodec':
        print(bintodec(input("number >>")))
    elif operation == 'bintoOct':
        print(bintoOct(input("number >>")))

helper(input("what operation: addition (add), subtraction (sub), multiplication (mult), division (div), power of (pwr), remainder (remain), binary To Decimal (bintodec), binary to octal (bintoOct) >>"))
