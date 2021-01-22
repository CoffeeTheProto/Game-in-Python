import math as m
import random as r

#Generate an enemy with random values relative to the player's stats
def generateEnemy():
    enemy = {}
    enemy["level"] = player["level"] + r.randint(-2,2) #Generate the level of the enemy
    #Make sure the level isn't less than 1
    if enemy["level"] < 1:
        enemy["level"] = 1
    enemy["health"] = 100 + (10 * enemy["level"]) #Generate the enemy health based on it's level
    #Generate four attacks for the enemy with random values
    enemy["attacks"] = (10 * r.randint(1,3), 10 * r.randint(1,3), 10 * r.randint(1,3), 10 * r.randint(1,3))
    return enemy

#Check the level of the player and update it if exp reaches 100
def checkLevel(exp):
    if exp >= 100:
        extra = exp - 100
        player["level"] += 1
        player["exp"] = extra

def battle():
    #Get the input to leave or stay in battle, and check it
    while True:
            choice = input("You have entered a battle. Roll for an attack. (y/n): ")
            choice.lower()
            if choice != "y" and choice != "n":
                continue
    if choice == "n":
        print("You have fled.")
    elif choice == "y":
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

#Play the tutorial
def tutorial():
    print(f"Welcome {player[name]}! In this tutorial, you will learn how to fight an enemy.")
    enemy = generateEnemy()


#Create the player
player = {}
player["name"] = input("Please enter your character's name: ")
player["level"], player["health"], player["exp"] = 1, 100, 0
player["attacks"] = (10 * r.randint(1,3), 10 * r.randint(1,3), 10 * r.randint(1,3), 10 * r.randint(1,3))

#Generate an enemy
enemy = generateEnemy()
print(enemy["level"])
print(enemy["attacks"])
