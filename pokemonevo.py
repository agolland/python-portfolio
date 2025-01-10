#Alexis Golland
#12/2/24
#Pokemon Evolution

#Init
import random
outcome = random.randint(1, 2)
pokemon_level = 1 #Global
pokemon_name = "Pidgey"
day = 1

#Functions
def train():
    global pokemon_level
    print("You did 30 jumpingjacks!")
    print("Your level increased by one!")
    pokemon_level = pokemon_level + 1
    print("Your pokemon level is now: " + str(pokemon_level))
def gym_battle():
    global pokemon_level
    global outcome
    if outcome == 1:
        print("You are up against Weedle!")
        print("You won! Your level increased by two!")
        pokemon_level = pokemon_level + 2
        print("Your pokemon level is now: " + str(pokemon_level))
    elif outcome == 2:
        print("You are up against Caterpie!")
        print("You lost. Your level decreased by one!")
        pokemon_level = pokemon_level - 1
        print("Your pokemon level is now: " + str(pokemon_level))
def evolve():
    global pokemon_level
    global pokemon_name
    if pokemon_level == 18:
        print("Your pokemon has evolved!")
        print("Your pokemons name is now: ")
        x = pokemon_name.replace("Pidgey","Pidgeotto")
        print(x)
    elif pokemon_level == 36:
        print("Your pokemon has evolved!")
        print("Your pokemons name is now: ")
        y = pokemon_name.replace("Pidgeotto","Pidgeot")
        print(y)
def rest():
    global pokemon_level
    global pokemon_name
    print("Your pokemon name is: " + str(pokemon_name))
    print("Your pokemon level is: " + str(pokemon_level))
    if pokemon_level >= 36:
        level36()
    elif pokemon_level >= 18:
        level16()
    elif pokemon_level < 18:
        level1()


#Main
print("Welcome to Pokemon Evolution")
while True:
    print("Select an activity for the day")
    print("""1. Train
2. Gym Battle
3. Rest (Display Info)
4. Quit""")
    activity = int(input("(1-4) Activity:"))
    if activity == 1: #True
        train()
        evolve()
    elif activity == 2:
        gym_battle()
        evolve()
    elif activity == 3:
        rest()
    elif activity == 4:
        break
