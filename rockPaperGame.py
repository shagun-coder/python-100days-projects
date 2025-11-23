import random
print("Wellcome to Rock Paper Scissors Game")
game_images = ["rock","paper","scissors"]
user_choice = int(input("what do you choose ? .Type 0 for Rock , 1 for paper , 2 for scissors\n"))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print(f"computer choice :")
print(game_images[computer_choice])
if user_choice >=3 or user_choice <= 0:
    print("Invald choice.you lose" )
if user_choice == 0 and computer_choice == "2":
    print("you  Win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose !")
elif computer_choice >user_choice:
    print("you lose !")
elif user_choice >computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("Tie")
          
           