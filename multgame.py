#Alexis Golland
#Period 3
#1/8/25

#Init
import random

#Functions
def questions():
    score = 0
    for i in range(5):
        num1 = random.randint(1,9)
        num2 = random.randint(1,9)
        print("What is " + str(num1) + " times " + str(num2))
        guess = int(input("What is your answer?"))
        if num1*num2 == guess:
            print("You are correct!")
            score = score + 1
            print("Your score went up! It is:")
            print(score)
        else:
            print("You are incorrect! Your score will stay the same")
            print(score)
    print("Your final score is:")
    print(score)

#Main
questions()

