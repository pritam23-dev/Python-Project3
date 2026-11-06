# Number guessing game

import random

RandomNumber = random.randrange(1,100)
userInput = int(input("Guess the number:"))

if userInput > RandomNumber:
    print(f"Random number:{RandomNumber }")
    print("The number is so high ⬆️")

elif RandomNumber > userInput:
    print(f"Random number:{RandomNumber }")
    print("The number is so low ⬇️")

else:
    print(f"Random number:{RandomNumber }")
    print("Yes, you matched the number 🤝")

