# f = open("Khata.txt", "w")
# f.write("চাল - ৫০ টাকা")
# f.close()
#
# f = open("Khata.txt", "r")
# print(f.read())
# f.close()
#
# f = open("Khata.txt", "a")
# f.write("\nডাল - ৮০ টাকা")
# f.close()
#
# f = open("Khata.txt", "r")
# print(f.read())
# f.close()
from random import choice
from sys import exception

# # ধাপ ৩: with দিয়ে ফাইল খোলা
# # f.write(...) লাইনটা একটু ডানে সরিয়ে (৪টা স্পেস বা Tab) লিখতে হয়।
# # Indentation (ভেতরে ঢোকানো)
# with open("khata.txt", "w", encoding="utf-8") as f:
#     f.write("চাল - ৫০ টাকা")     # ← এটা ভেতরে, ফাইল খোলা আছে
#     f.write("\nডাল - ৮০ টাকা")   # ← এটাও ভেতরে
#
# print("কাজ শেষ")                 # ← এটা বাইরে, ফাইল এখন বন্ধ

# with open("khata.txt", "w", encoding="utf-8") as f:
#     f.write("চাল - ৫০ টাকা")
#
# with open("khata.txt", "a", encoding="utf-8") as f:
#     f.write("\nডাল - ৮০ টাকা ")
#     f.write("\nতেল - ১৪০ টাকা")

# # উপায় ১: read() (পুরোটা একসাথে)
# with open("khata.txt", "r", encoding="utf-8") as f:
#     print(f.read())

# # উপায় ২: readline() (একবারে একটা লাইন)
# with open("Khata.txt", "r") as f:
#     line1 = f.readline()
#     line2 = f.readline()
# print(line1)
# print(line2)

# উপায় ৩: for লুপ দিয়ে লাইন ধরে ধরে (সবচেয়ে বেশি ব্যবহৃত)
# with open("Khata.txt", "r") as f:
#     for line in f:
#         print(line)
#
# with open("Khata.txt", "r") as f:
#     for line in f:
#         print(line.strip())   # সমাধান: strip() দিয়ে \n কেটে ফেলা।

# jodi only line 2 read korte cai tokhon koronio ⬇️

# # উপায় ১: readline() ২ বার (সবচেয়ে সহজ)
# with open("khata.txt", "r", encoding="utf-8") as f:
#     f.readline()            # ১ম লাইন পড়লাম, কিন্তু ফেলে দিলাম
#     line2 = f.readline()    # ২য় লাইন এটাই চাই
# print(line2.strip())

# # উপায় ২: for লুপ + গণনা (বড় ফাইলে কাজে লাগে)
# with open("khata.txt", "r", encoding="utf-8") as f:
#     for number, line in enumerate(f, start=1):
#         if number == 2:
#             print(line.strip())
#             break

# # উপায় ৩: সব লাইন list-এ নিয়ে index দিয়ে (সবচেয়ে ছোট)
# with open("khata.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()        # Focus = s
# print(lines[2].strip())


#### ধাপ ৫: Error Handling শুরু, try / except ⬇️⬇️⬇️
# with open("hisab.txt", "r", encoding="utf-8") as f:
#     print(f.read())
# # FileNotFoundError: [Errno 2] No such file or directory: 'hisab.txt'

# # ফাইল নেই (hisab.txt):
# try:
#     with open("hisab.text", "r", encoding="utf-8") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("ফাইলটা পাওয়া যায়নি!")

# # ফাইল আছে (khata.txt):
# try:
#     with open("Khata.txt", "r", encoding="utf-8") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("ফাইলটা পাওয়া যায়নি!")

# 1. ValueError (ভুল ধরনের মান)
# 2. ZeroDivisionError (শূন্য দিয়ে ভাগ)
# 3. সব Error একসাথে ধরা (Exception)
# কোন Error হবে জানা না থাকলে সব ধরনের Error ধরার উপায়:

# try:
#     taka = int(input("মোট টাকা?"))
#     jon = int(input("কতজন?"))
#     print("প্রত্যেকে পাবে:", taka / jon)
# except ValueError:
#     print("দয়া করে শুধু সংখ্যা লিখুন!")
# except ZeroDivisionError:
#     print("০ দিয়ে ভাগ করা যায় না!")
# except Exception:
#     print("কিছু একটা ভুল হয়েছে!")


# try:
#     f = open("hisab.txt", "r", encoding="utf-8")
#     print(f.read())
# except FileNotFoundError:
#     print("ফাইলটা পাওয়া যায়নি!")
# finally:
#     print("কাজ শেষ, দোকান বন্ধ।")

# f = None
# try:
#     f = open("khata.txt", "r", encoding="utf-8")
#     print(f.read())
# except FileNotFoundError:
#     print("ফাইলটা পাওয়া যায়নি!")
# finally:
#     if f:
#         f.close()
#         print("ফাইল বন্ধ করা হলো।")

### ধাপ ৮: সব মিলিয়ে পূর্ণ প্রোগ্রাম, দোকানের হিসাব

# def hisab_likho():
#     naam = input("জিনিসের নাম: ")
#     try:
#         dam = int(input("দাম (টাকা): "))
#     except ValueError:
#         print("দয়া করে দামের জায়গায় শুধু সংখ্যা লিখুন!")
#         return
#
#     with open("Khata.txt", "a", encoding="utf-8") as f:
#         f.write(f"{naam} - {dam} টাকা\n")
#     print("হিসাব সেভ হয়েছে ✅")
#
#
# def hisab_dekho():
#     try:
#         with open("khata.txt", "r", encoding="utf-8") as f:
#             print("--- আজকের হিসাব ---")
#             for line in f:
#                 print(line.strip())
#     except FileNotFoundError:
#         print("এখনো কোনো হিসাব নেই। আগে কিছু লিখুন।")
#
#
# try:
#     hisab_likho()
#     hisab_dekho()
# finally:
#     print("ধন্যবাদ, দোকান বন্ধ।")

###

# def hisab_likho():
#     naam = input("জিনিসের নাম: ")
#     try:
#         dam = int(input("দাম (টাকা): "))
#         if dam <= 0:
#             raise ValueError("দাম ০ বা ঋণাত্মক হতে পারে না")
#     except ValueError as e:
#         print("সমস্যা:", e)
#         return
#
#     with open("Khata.txt", "a", encoding="utf-8") as f:
#         f.write(f"{naam} - {dam} টাকা\n")
#     print("হিসাব সেভ হয়েছে ✅")

####

def hisab_likho():
    naam = input("জিনিসের নাম: ")
    try:
        dam = int(input("দাম (টাকা): "))
        if dam <= 0:
            raise ValueError("দাম ০ বা ঋণাত্মক হতে পারে না")
    except ValueError as e:
        print("সমস্যা:", e)
        return

    with open("Khata.txt", "a", encoding="utf-8") as f:
        f.write(f"{naam} - {dam} টাকা\n")
    print("হিসাব সেভ হয়েছে ✅")


def hisab_dekho():
    try:
        with open("khata.txt", "r", encoding="utf-8") as f:
            print("--- আজকের হিসাব ---")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("এখনো কোনো হিসাব নেই। আগে কিছু লিখুন।")


try:
    print("1. হিসাব লিখুন")
    print("2. হিসাব দেখুন")
    choice = input("আপনার পছন্দ (1 বা 2): ")

    if choice == "1":
        hisab_likho()
    elif choice == "2":
        hisab_dekho()
    else:
        print("ভুল পছন্দ! শুধু 1 বা 2 দিন।")

finally:
    print("ধন্যবাদ, দোকান বন্ধ।")
















