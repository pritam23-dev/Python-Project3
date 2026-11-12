# # project_1 number guessing game_2
#
# secret = 42
# tries = 0
#
# while True:
#     guess = int(input("Guess a number between 1 and 100 :"))
#     tries += 1
#     if guess > secret :
#         print("It's too big, give me a smaller one.")
#     elif guess < secret :
#         print("It's too small, give me a bigger one.")
#     else:
#         print("Correct! You did it in 3 attempts.")
#         break


# # প্রজেক্ট ২: জোড়-বিজোড় গুনতি 🔢
# # গল্প: ১ থেকে ১০ পর্যন্ত সংখ্যার মধ্যে বিজোড় সংখ্যা বাদ দিয়ে শুধু জোড় সংখ্যাগুলো print করো, আর ৮ এ পৌঁছে থামো।
#
# for i in range(1,11):
#     if i % 2 != 0:
#         continue
#     print(i)
#     if i == 8:
#         break

# # প্রজেক্ট ৩: নামতা ছাপানো 📒
# # গল্প: ব্যবহারকারী একটা সংখ্যা দেবে, তুমি তার নামতা ১ থেকে ১০ পর্যন্ত দেখাবে।
#
# n = int(input("কত এর নামতা চাও? ans:"))
# for i in range(1,11):
#     print(n,"x",i,"=",n * i)

# কাজ: ১ থেকে ২০ পর্যন্ত সংখ্যা print করো, কিন্তু:
#
# যে সংখ্যা ৩ দিয়ে ভাগ যায়, সেটা বাদ দাও (continue)
# সংখ্যা 14 হলে থামো (break)

for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)
    if i == 14:
        break





