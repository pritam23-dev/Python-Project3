import random

RandomNumber = random.randrange(1,100)
userInput = int(input("Guss the number:"))

if userInput > RandomNumber:
    print(RandomNumber)
    print("The number is so high ⬆️")

elif RandomNumber > userInput:
    print(RandomNumber)
    print("The number is so low ⬇️")

else:
    print(RandomNumber)
    print("Yes, you matched the number 🤝")

