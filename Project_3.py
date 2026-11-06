# Text based adventure game project

answer = input("Do you want to play this game? [yes/no]:")

if answer == "yes":
    print("Welcome to the game!")
    answer = input("Do you want to go to the jungle or a cave? [jungle/cave]:")
    if answer == "jungle":
        print("You saw a hungry tiger(🐯) and the tiger ate you. your game is over.")
    elif answer == "cave":
        print("You saw a bear(🐻) in front of cave.")
        answer = input("Do you want to fight with the bear or run away? [fight/run]")
        if answer == "fight":
            print("The bear is too much strong! you lose the game.")
        else:
            print("Wow, still you are alive!")

else:
    print("The game closed.")


