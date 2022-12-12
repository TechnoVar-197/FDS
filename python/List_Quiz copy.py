import random
print("Welcome to Number list test Program")


def Questions(x):
    if (x == 1):
        x = random.sample(range(10, 25), 7)
        q3 = int(input("What is the smallest element of this list ?{}\n".format(x)))
        if q3 == min(x):
            print("correct !")
            score = score+1
        else:
            print("incorrect !")
    if (x == 2):
        x = random.sample(range(10, 25), 7)
        q4 = int(input("What is the biggest number in the list ?{}\n".format(x)))
        if q4 == max(x):
            print("correct !")
            score = score+1
        else:
            print("incorrect !")
    if (x == 3):
        x = random.sample(range(10, 25), 7)
        q1 = int(
            input("What is the sum of first and last elements in the list ?{}\n".format(x)))
        if q1 == x[0]+x[-1]:
            print("correct !")
            score = score+1
        else:
            print("incorrect !")
    if (x == 4):
        x = random.sample(range(10, 25), 7)
        y = random.sample(range(1, 5), 1)
        index = y[0]-1
        q2 = int(input(
            "what is the sqaure of {}th element of the list ? {}\n".format(index+1, x)))
        if q2 == (x[index]**2):
            print("correct !")
            score = score+1
        else:
            print("incorrect !")
    if (x == 5):
        x = random.sample(range(10, 25), 7)
        q2 = int(input("what is the sum of numbers in the list ?{}\n".format(x)))
        if q2 == sum(x):
            print("correct !")
            score = score+1
        else:
            print("incorrect !\nThe answer is {}".format(sum(x)))
    if (x == 6):
        x = random.sample(range(20, 50), 7)
        y = random.sample(range(1, 5), 1)
        index = y[0]-1
        q4 = int(input(
            "What is the element at index value {} in the list ?{}\n".format(index+1, x)))
        if q4 == x[index]:
            print("correct !")
            score = score+1
        else:
            print("incorrect !")
while(True):
    print("Hello World")
