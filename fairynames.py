#Name Generator
#Alexis Golland
#10/21/24

#Init

#Functions
print("Welcome to your Fairy Name 2000")
print("Answer the questions to find out your fairy name")
ans = input("summer (sum) or winter (win) ?")
if ans == "sum":
    ans = input("Sour (sou) or Sweet (swe) ?")
    if ans == "sou":
        ans = input("Gummyworms (gum) or LemonShortcake (cake) ?")
        if ans == "gum":
            print("Your name is YummyGummy")
        else:
            print("Your name is Lele")
    if ans == "swe":
        ans = input("Popsicles (pop) or Cupcakes (cup) ?")
        if ans == "pop":
            print("Your name is Poppy")
        else:
            print("Your name is Cuppy")
if ans == "win":
    ans = input("Cranberries (cran) or Snickerdoodles (snick) ?")
    if ans == "cran":
        ans = input("Cranberrypie (pie) or Cranberryjuice (juc) ?")
        if ans == "pie":
            print("Your name is Piper")
        else:
            print("Your name is CrannyFrany")
    if ans == "snick":
        ans = input("Cookie (cook) or Cinnamon (cinna) ?")
        if ans == "cook":
            print("Your name is Doodlie")
        else:
            print("Your name is Sweet n, Spiced")

#Main
