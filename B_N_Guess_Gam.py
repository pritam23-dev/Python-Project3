# # Number Guessing Game Type_1💫
#
# import random
#
# while True:
#     randomNum = random.randint(1, 5)
#     while True:
#         try:
#             userInp = int(input("Guess the number: "))
#             if 1<= userInp <= 5:
#                 break
#             print("Please, enter a number between 1 and 5!")
#         except ValueError:
#             print("Please enter a number!")
#
#     print(f"Random number is: {randomNum}")
#     if randomNum == userInp:
#         print("You win!")
#     else:
#         print("You lose!")
#
#     while True:
#         again = input("Do you want to play again? ( y/n ): ").lower()
#         if again == "y" or again == "n":
#             break
#         print("Please, enter y/n !")
#
#     if again == "n":
#         print("Goodbye")
#         break




# # Number Guessing Game Type_2💫
#
# import random
#
# while True:
#     maxAttempt = 5
#     maxNum = 20
#     print(f"I'm thinking of a number between 1 and {maxNum}. You have {maxAttempt} attempts.\n")
#     secret = random.randint(1, maxNum)
#     won = False
#
#
#     for attempt in range(1, maxAttempt + 1):
#
#         while True:
#             try:
#                 userInp = int(input(f"Attempt {attempt}/{maxAttempt} - Guess the number: "))
#                 if 1<= userInp <= maxNum:
#                     break
#                 print(f"Please, enter a number between 1 and {maxNum}!")
#             except ValueError:
#                 print("Please enter a number!")
#
#
#         if userInp == secret:
#             if attempt == 1:
#                 print("Wow!💫 You win! you guessed it in 1💫 attempt")
#             else:
#                 print(f"You win! You guessed it in {attempt} attempts.")
#             won = True
#             break
#         elif userInp < secret:
#             print("Too low! Try higher.")
#         else:
#             print("Too high! Try lower.")
#
#     if not won:
#         print(f"You lose! The number was {secret}.")
#
#
#     while True:
#         again = input("Do you want to play again? ( y/n ): ").lower()
#         if again == "y" or again == "n":
#             break
#         print("Please, enter y/n !")
#
#     if again == "n":
#         print("Goodbye!")
#         break


# Number Guessing Game Type_2💫 by Function 🐍

import random


def get_guess(attempt, maxAttempt, maxNUm):
    while True:
        try:
            userInp = int(input(f"Attempt {attempt}/{maxAttempt} - Guess the number: "))
            if 1 <= userInp <= maxNUm:
                return userInp
            print(f"Please, enter a number between 1 and {maxNUm}")
        except ValueError:
            print("Please, enter a number!")


def ask_play_again():
    while True:
        again = input("Do you want to play again? ( y/n ): ").lower()
        if again == "y":
            return True
        elif  again == "n" :
            return False
        else:
            print("Please, enter y/n !")


def play_round(max_Attempt, max_Num):
    secret = random.randint(1, max_Num)
    print(f"I'm thinking of a number between 1 and {max_Num}. You have {max_Attempt} attempts.\n")

    for attempt in range(1, max_Attempt + 1):
        userInp = get_guess(attempt, max_Attempt, max_Num)

        if userInp == secret:
            if attempt == 1:
                print(f"Wow!💫 You win! you guessed it in 1💫 attempt")
            else:
                print(f"You win! You guessed it in {attempt} attempts.")
            return

        elif userInp < secret:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")

    print(f"You lose! The number was {secret}.")


# ===== মূল প্রোগ্রাম =====
while True:
    play_round(5,20)
    print()
    if not ask_play_again():
        print("Goodbye!")
        break




