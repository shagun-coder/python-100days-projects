print("Welcome to Treasure Island!")
print("Your mission is to find the Treasure.")

at_cross_road = input('You’re at the cross road. Where do you want to go? Type "left" or "right": ').lower()

if at_cross_road == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    action = input('Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()

    if action == "wait":
        final_step = input("Final level! Choose one door: Red, Blue, Yellow: ").lower()

        if final_step == "red":
            print("It's a room full of fire. Game over!")
        elif final_step == "blue":
            print("You enter a room full of beasts. Game over!")
        elif final_step == "yellow":
            print("You found the treasure! You win! 🎉")
        else:
            print("Invalid door. Game over!")
    else:
        print("You got attacked by a crocodile. Game over.")

else:
    print("You fell into a hole. Game over.")
