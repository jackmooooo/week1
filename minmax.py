print('welcome to my calculator')
def helper():
    inputing = True
    array = []
    while inputing == True:
        array.append(input("first number  >> "))
        if input("want another number?  >> ") == "yes":
            inputing = True
        else:
            inputing = False
    min(array)
    max(array)

def min(arr):
    min = arr[0]
    minindex = 0
    for i in range(len(arr)):
        if arr[int(i)] < min:
            min = arr[int(i)]
            minindex = i
        return min
    print("your smallest number is " + str(min))
    print("at index " + str(minindex))

def max(arr):
    max = arr[0]
    maxindex = 0
    for i in range(len(arr)):
        if arr[int(i)] > max:
            max = arr[int(i)]
            maxindex = i
    print("your highest number was " + str(max))
    print("the index is " + str(maxindex))

helper()
