#Alexis Golland
#Guessing Game
#11/11/24
#Period 3

#init
import random
#functions
def mode():
    print("Welcome player to the Guessing Game, you get 3 tries!") #Prints welcome statement and amount of tries
    secret = random.randint(0,10)
    for i in range(3): #three tries
        guess = int(input("Please guess a number from 1 to 10")) #range from 1 to 10
        print(guess)
        if guess == secret:#answer is correct
            print("Your guess is correct!")

        else:
            if guess > secret:#answer is wrong,requirements to try again
                print("You guessed too high, try again!")
            else: print("You guessed too low, try again!")


#main
mode()

