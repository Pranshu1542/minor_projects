from art_treasure import *
print(logo)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")

choice1 = input("Type 'left' or 'right' : ")
if choice1 == "left":
    choice2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across : ")
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if choice3 == "red":
            print("It's a room full of fire.\nGame Over.")
        elif choice3 == "yellow":
            print("You found the treasure!\nYou Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts.\nGame Over.")
        else:
            print("You chose a door that doesn't exist.\nGame Over.")
    elif choice2 == "swim":
        print("You get attacked by an angry trout.\nGame Over.")
    else:
        print("Invalid choice.\nGame Over.")

elif choice1 == "right":
    print("You fell into a hole.\nGame Over.")
else:
    print("Invalid choice.\nGame Over.")
