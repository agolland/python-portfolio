#Slot Machine
#Alexis Golland & Saisha Kapoor

#Init
import random
import time
symbols = ["❀","✿", "❁", "✾", "7"]

#Functions
def intro():
        print("Welcome to the 3 Slot Machine! You have 100 credits, each spin costs 10 credits!")
        print("Select 'S' to spin and 'Q' to Quit")
def playGame():
    credits=100
    while True:
        try:
             keepGame = input("S or Q?")
        except:
            print("ERROR! Select CAPITAL 'S' or 'Q'")
        if keepGame == "S":
            print("One spin costs 10 credits")
            print("You have this many credits now")
            credits = credits-10
            if credits <= 0:
                        print("You do not have enough credits to play, thank you for using Slot Machine!")
                        break
            print(credits)
            print("Spinning...")
            time.sleep(3)
            slot1 = random.choice(symbols)
            slot2 = random.choice(symbols)
            slot3 = random.choice(symbols)
            if slot1 == 7 and slot2 == 7 and slot3==7:
                print("Congrats! You hit Jackpot and got three 7's in a row!")
            elif slot1 == "❀" and slot2 == "❀" and slot3 =="❀":
                print("Congrats! You win! You got three matching symbols in a row!")
            elif slot1 == "✿" and slot2 == "✿" and slot3 == "✿":
                print("Congrats! You win! You got three matching symbols in a row!")
            elif slot1 == "❁" and slot2=="❁" and slot3=="❁":
                print("Congrats! You win! You got three matching symbols in a row!")
            elif slot1 == "✾" and slot2=="✾" and slot3=="✾":
                print("Congrats! You win! You got three matching symbols in a row!")
            elif slot1==slot2:
                 print("Congrats! You got a pair! You partially won the game!")
            elif slot1==slot3:
                 print("Congrats! You got a pair! You partially won the game!")
            elif slot2==slot3:
                 print("Congrats! You got a pair! You partially won the game!")
            else:
                print("Sorry, you lost the game.")

            print("Would you like to play again?")
            try:
                playAgain = input("yes or no")
            except:
                print("ERROR! Please enter yes or no, using lowercase letters!")
            if playAgain == "yes":
                    print("Your credits will display here:")
                    print(credits)
            else:
                 print("Finishing game...")
                 break
        else:
            print("Finishing game...")
            break
#Main
intro()
playGame()
