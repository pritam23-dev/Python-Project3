import random

DiceRolling = True

while DiceRolling:
    print(random.randint(1,6))
    PlayAgain = input("Do you want to Roll again? [ y/n ]: ")
    if PlayAgain == "y":
        continue
    else:
        print("Game over.")
        break



