import math as m
import random as r

#Generate an enemy with random values relative to the player's stats
def generateEnemy():
    enemy = {}
    enemy["lvl"] = player["lvl"] + r.randint(-2,2) #Generate the level of the enemy
    #Make sure the level isn't less than 1
    if enemy["lvl"] < 1:
        enemy["lvl"] = 1
    enemy["health"] = 100 + (10 * enemy["lvl"]) #Generate the enemy health based on it's level
    enemy["attacks"] = (10 * r.randint(1,3), 10 * r.randint(1,3), 10 * r.randint(1,3), 10 * r.randint(1,3)) #Generate four attacks for the enemy with random values
    #Print the stats of the enemy
    print(f"\nEnemy level: {enemy['lvl']}")
    print(f"Enemy health: {enemy['health']}")
    print("Enemy Attacks:")
    print(f"    Attack 1: {enemy['attacks'][0]}")
    print(f"    Attack 2: {enemy['attacks'][1]}")
    print(f"    Attack 3: {enemy['attacks'][2]}")
    print(f"    Attack 4: {enemy['attacks'][3]}")
    return enemy

#Check the level of the player and update it if exp reaches 100
def checkLevel(exp):
    if exp >= 100:
        extra = exp - 100
        player["lvl"] += 1
        player["exp"] = extra

def battle():
    #Get the input to leave or stay in battle, and check it
    while True:
        choice = input("You have entered a battle. Roll for an attack. (y/n): ")
        choice.lower()
        if choice == "n":
            print("You have fled")
            return
        elif choice == "y":
            break
        else:
            print("Invalid input. Please try again.")
            continue
    enemy = generateEnemy()
    while enemy["health"] > 0 and player["health"] > 0:
        #Randomly choose the attack that the player should use
        randomAttack = r.randint(1,4)
        if randomAttack == 1:
            enemy["health"] -= player["attacks"][0]
        elif randomAttack == 2:
            enemy["health"] -= player["attacks"][1]
        elif randomAttack == 3:
            enemy["health"] -= player["attacks"][2]
        elif randomAttack == 4:
            enemy["health"] -= player["attacks"][3]
        #Check if the enemy has died
        if enemy["health"] <= 0:
            while enemy["health"] < 0:
                enemy["health"] += 10
            print(f"\nYou have done {player['attacks'][randomAttack - 1]} damage. \n-Your health: {player['health']} \n-Enemy health: {enemy['health']}")
            print("The enemy is dead. You have won!")
            return True
        print(f"\nYou have done {player['attacks'][randomAttack - 1]} damage. \n-Your health: {player['health']} \n-Enemy health: {enemy['health']}")
        #Randomly choose the attack that the enemy should use
        randomAttack = r.randint(1,4)
        if randomAttack == 1:
            player["health"] -= enemy["attacks"][0]
        elif randomAttack == 2:
            player["health"] -= enemy["attacks"][1]
        elif randomAttack == 3:
            player["health"] -= enemy["attacks"][2]
        elif randomAttack == 4:
            player["health"] -= enemy["attacks"][3]
        #Check if the player has died
        if player["health"] <= 0:
            while player["health"] < 0:
                player["health"] += 10
            print(f"\nEnemy has done {enemy['attacks'][randomAttack - 1]} damage. \n-Your health: {player['health']} \n-Enemy health: {enemy['health']}")
            print(f"player['name'] has died. Game Over.")
            return False
        print(f"\nEnemy has done {enemy['attacks'][randomAttack - 1]} damage. \n-Your health: {player['health']} \n-Enemy health: {enemy['health']}")
        #Ask the player if they want to continue
        while True:
            choice = input("\nContinue? (y/n): ")
            choice.lower()
            if choice == "n":
                print("You have fled")
                return
            elif choice == "y":
                break
            else:
                print("Invalid input. Please try again.")
                continue
#Play the tutorial
def tutorial():
    print(f"Welcome, {player['name']}! In this tutorial, you will learn how to fight an enemy.")
    if battle():
        print(f"Congratulations {player['name']}! You have beat the tutorial. You can now progress to the rest of the game. Good luck!")

#Create the player
player = {}
player["name"] = input("Please enter your character's name: ")
player["lvl"], player["health"], player["exp"] = 1, 100, 0
player["attacks"] = ((10 * r.randint(1,3)) + 10, (10 * r.randint(1,3)) + 10, (10 * r.randint(1,3)) + 10, (10 * r.randint(1,3)) + 10)
tutorial()
