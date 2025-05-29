#Alexis Golland
#Magic 8 Ball
# 1/24/25
#Period 3

#Init
import random
responses = ["Of Course", "Surely", "Very Probable", "Very Likely", "100 Percent","It's Likely", "Maybe", "Could be", "Possibly", "Could happen", "Never", "Very Unlikely", "Not Happening", "Not At All", "Nope"]

#Functions
def Magicball():
    print("Welcome to Magic 8 Ball!")
    keepGoing = "yes"
    while keepGoing != "no":
        question = (input("Please give me a yes or no question"))
        print(question)
        if question.endswith("?"):
            print(random.choice(responses))
        else:
            print("Error! Please give me a yes or no question with a question mark")
        keepGoing = (input("Do you want to keep playing?"))
        print(keepGoing)
        if keepGoing == "yes":
            question2 = (input("Please give me another yes or no question"))
            print(question2)
            if question.endswith("?"):
                print(random.choice(responses))
            else:
                print("Error! Please give me a yes or no question with a question mark")
        if keepGoing == "no":
            print("Thank you for playing Magic 8 Ball!")
            break

#Main
Magicball()

