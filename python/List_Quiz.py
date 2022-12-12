import random
print("Welcome to Number list test Program")

while True:
    print("Select a Difficulty:\n")
    n=input("[E]asy\n[M]edium\n[H]ard\n")
    if (n=="H" or n=="h"):
        print("Hard difficulty level selected")
        print("Question 1 of 6")
        score=0
        x=random.sample(range(10,25),7)
        q1=int(input("What is the sum of first and last elements in the list ?{}\n".format(x)))
        if q1==x[0]+x[-1]:
            print("correct !")
            score=score+1
        else:
            print("incorrect !")
        print("Question 2 of 6")
        x=random.sample(range(10,25),7)
        y=random.sample(range(1,5),1)
        index=y[0]-1
        q2=int(input("what is the sqaure of {}th element of the list ? {}\n".format(index+1,x)))
        if q2==(x[index]**2):
            print("correct !")
            score=score+1
        else:
            print("incorrect !")
        print("Question 3 of 6")
        x=random.sample(range(10,25),7)
        q3=int(input("What is the smallest element of this list ?{}\n".format(x)))
        if q3==min(x):
            print("correct !")
            score=score+1
        else:
            print("incorrect !")
        print("Question 4 of 6")
        x=random.sample(range(10,25),7)
        q4=int(input("What is the biggest number in the list ?{}\n".format(x)))
        if q4==max(x):
            print("correct !")
            score=score+1
        else:
            print("incorrect !")
        print("Question 5 of 6")
        x=random.sample(range(10,25),7)
        q2=int(input("what is the sum of numbers in the list ?{}\n".format(x)))
        if q2==sum(x):
            print("correct !")
            score=score+1
        else:
            print("incorrect !\nThe answer is {}".format(sum(x)))  
        print("Question 6 of 6")
        print("Challenge Question")
        x=random.sample(range(20,50),7)
        y=random.sample(range(1,5),1)
        index=y[0]-1
        q4=int(input("What is the element at index value {} in the list ?{}\n".format(index+1,x)))
        if q4==x[index]:
            print("correct !")
            score=score+1
        else:
            print("incorrect !")
        print("Test Complete!")
        print("Your score= {}/6".format(score))
        print("Your percentage={}".format((score/6)*100))
        exit()
    elif (n=="E" or n=="e"):
        print("Easy difficulty level selected")
        score=0
        print("Question 1 of 2")
        x=random.sample(range(1,5),3)
        q1=int(input("What is the first element of this list ?{}\n".format(x)))
        if q1==x[0]:
            print("correct !")
            score=score+1
        else:
            print("incorrect !")
        print("Question 2 of 2")
        x=random.sample(range(1,5),3)
        q2=int(input("last element of this list ?{}\n".format(x)))
        if q2==x[-1]:
            print("correct !")
            score=score+1
        else:
            print("incorrect !")
        print("Test Complete!")
        print("Your percentage={}".format((score/2)*100))
        exit()

    elif (n=="M" or n=="m"):
        print("Medium difficulty level selected")
        score=0
        print("Question 1 of 4")
        x=random.sample(range(5,15),5)
        q1=int(input("What is the highest number  in the list ?{}\n(roundup to nearest integer)\n".format(x)))
        if q1==max(x):
            print("correct !")
            score=score+1
        else:
            print("incorrect !")
        print("Question 2 of 4")
        x=random.sample(range(5,15),5)
        q2=int(input("what is the sum of numbers in the list ?{}\n".format(x)))
        if q2==sum(x):
            print("correct !")
            score=score+1
        else:
            print("incorrect !\nThe answer is {}".format(sum(x)))
        print("Question 3 of 4")
        x=random.sample(range(5,15),5)
        y=random.sample(range(1,5),1)
        index=y[0]-1
        q3=int(input("What number is at position {} in the list ?{}\n(roundup to nearest integer)\n".format(index+1,x)))
        if q3==x[index]:
            print("correct !")
            score=score+1
        else:
            print("incorrect !")
        print("Question 4 of 4")
        print("Challenge Question !")
        x=random.sample(range(10,30),5)
        q4=int(input("What is the difference between the lowesmt and highest numbers in the list ?{}\n".format(x)))
        if q4==max(x)-min(x):
            print("correct !")
            score=score+1
        else:
            print("incorrect !")
        print("Test Complete!")
        print("Your score= {}/4".format(score))
        print("Your percentage={}".format((score/4)*100))
        exit()
    else:
        print("Invalid choice! Enter E,M or H.\n")