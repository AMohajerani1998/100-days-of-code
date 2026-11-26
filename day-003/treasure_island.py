print("Welcome to Treasure Island. Your mission is to find the treasure.")

move1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()

if move1 == "right":
    print("You fell into a hole. Game Over!")
elif move1 == "left":
    move2 = input("You reached a lake and there's an island in the middle of the lake. Type \"wait\" to wait for a boat. type \"swim\" to swim across. ").lower()
    if move2 == "swim":
        print("You got attacked by an angry trout. Game Over!")
    elif move2 == "wait":
        move3 = input("You reached a room with 3 colored doors. Which door will you choose? red/blue/yellow: ").lower()
        if move3 == "blue" or move3 == "red":
            if move3 == "blue":
                print("You enter a room of beasts. Game Over!")
            elif move3 == "red":
                print("It's a room full of fire. Game Over!")
        elif move3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("That door doesn't exist. Game Over.")
    else:
        print("You entered a wrong input. Please try again.")
else:
    print("You entered a wrong input. Please try again.")