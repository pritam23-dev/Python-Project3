# Slicing (স্লাইসিং)
# word = "PROGRAMMING"
#
# print(word[0:3])
# print(word[3:7])
# print(word[:3])
# print(word[7:])
# print(word[:])
# print(word[-4:])
#
# phone = "01987654321"
# print(phone[-4:])
# print(phone[0:10:2])   # Step ( লাফ দিয়ে নেওয়া)
# print(phone[0:10:3])
#
# city = "Madaripur"
# print(city[::-1])


# name = "pritam"
# print(name.upper())
#
# Name = "PRITAM"
# print(Name.lower())
#
# email = "Pritam@gmail.com"
# print(email.lower())
#
# # Real life উদাহরণ ২: Password/Yes-No চেক
# # ইউজার কেউ "YES" লিখল, কেউ "yes", কেউ "Yes"। সবাইকে এক করে নিতে:
#
# Answer = "YeS"
# if Answer.lower() == "yes":
#     print("তুমি রাজি আছো!")
#
# # Real life উদাহরণ ৩: Heading বানানো
#
# title = "welcome to my website"
# print(title.upper())

# name = "pritam"
# name = name.upper()
# print(name)


# strip(): শুরু আর শেষের বাড়তি ফাঁকা জায়গা (space) কেটে ফেলে

# name = "   Pritam   "
# print(name.strip())

# Real life উদাহরণ: Login
# ইউজার username দিল " pritam " (আগে-পরে space)। এটা পরিষ্কার না করলে ডাটাবেসের "pritam" এর সাথে মিলবে না!

# username = "    Pritam    "
# if username.strip() == "Pritam":
#     print("login সফল!")
#
# text = "   Hello world   "
# print(text.strip())
# # print(text.lstrip())
# # print(text.rstrip())

# replace(): কোনো অংশ বদলে অন্য কিছু বসায়

# text = " I love Java"
# print(text.replace("Java","Python"))
#
# comment = "This is a bad movie"
# print(comment.replace("bad","***") )
#
# phone = "017-1234-5678"
# print(phone.replace("-",""))
#
# Text = "banana"
# print(Text.replace("a","o",2))
#
# text = "hello"
# text.replace("h", "j")
# print(text)          # hello (বদলায়নি)
#
# text = text.replace("h", "j")
# print(text)          # jello (এবার বদলেছে)

# split(): string ভেঙে List বানায়
#
# text = "apple banana mango"
# print(text.split())
#
#
# full_name = "Pritam kumar das"
# parts = full_name.split()
#
# print(parts)
# print(parts[0])
#
# fruits = "apple, banana, mango"
# print(fruits.split(","))
#
# email = "pritam@gmail.com"
# x = email.split("@")
# print(x[0])
# print(x[1])
#
# sentence = "I am learning python"
# word = sentence.split()
# print(len(word))


# join(): List জোড়া লাগিয়ে string বানায়

# word = ["I", "love", "Python"]
# y = " ".join(word)
# print(y)
#
# # বিভিন্ন চিহ্ন দিয়ে জোড়া
#
# Word = ["2026", "11", "08"]
# print("-".join(Word))
# print("/".join(Word))
# print(".".join(Word))
# print("".join(Word))
# print(" ".join(Word))
# # তারিখ সাজানো
# day = "08"
# month = "11"
# year = "2026"
#
# date = "/".join([day,month,year])
# print(date)
#
# # Hashtag বানানো
#
# tags = ["pyton", "coding","bangladesh"]
# print(" #".join(tags))

# দুইটা একসাথে ব্যবহার split , join

# title = "My First Python Blog"
# word = title.split()
#
# url = "-".join(word).lower()
# print(url)

# join() শুধু string-এর list জোড়া দিতে পারে। সংখ্যা থাকলে error আসে:
# nums = [1, 2, 3]
# print("-".join(nums))

# # ঠিক করতে সংখ্যাগুলো আগে string বানাতে হবে:
# nums = ["1", "2", "3"]
# print("-".join(nums))
# print(" ".join(nums))

# # split আর join একে অপরের উল্টো
#
#
# text = "red,green,blue"
# print(text.split(","))
#
# x = ["Madaripur", "Dhaka", "Bangladesh"]
# print(", ".join(x))

# f-string Formatting

# name = "Pritam"
# city = "Madaripur"
#
# print("আমার নাম " + name + ", আমি " + city + "-এ থাকি।")
#
# Name = "Pritam"
# City = "Madaripur"
# print(f"My name is {Name}, I live in {City}.")

# age = 20 # aivhabe int str a conver hoy na
# print("I am " + age + "years old.")

# age = 20
# print(f"I am {age} years old.")
#
# item = "Notebook"
# price = 50
# quantity = 3
# print(f"{item} এর দাম {price} টাকা, {quantity} টা নিলে মোট {price * quantity} টাকা")  # { } এর ভেতরে হিসাবও করা যায়!

# Method-ও ব্যবহার করা যায়

# name = "pritam"
# print(f"Hello {name.upper()}")

# দশমিকের পর কয়টা ঘর দেখাবে
# {মান:.2f} লিখলে দশমিকের পর ২ ঘর দেখায়:

# price = 99.5645
# print(f"দাম :{price:.3f}")
#
# # হাজারে কমা বসানো { variable:, }
# Salary = 150000
# print(f"Salary: {Salary:,}")

# মনে রাখার পয়েন্ট
# শুরুতে f লাগবে: f"..."
# Variable রাখো { } এর ভেতরে
# সংখ্যা নিজে থেকেই string হয়ে যায়
# { } এর ভেতরে হিসাব ও method চলে
# {মান:.2f} → ২ ঘর দশমিক
# {মান:,} → হাজারে কমা

# Price = 49.999
# print(f"price: {Price:.2f}")

# task...
# full_name = "   pritam kumar das   "
# strip() দিয়ে space কাটো
# split() দিয়ে ভাঙো
# প্রথম নামটা নাও, upper() করো
# f-string দিয়ে print করো: Hello, PRITAM! Welcome.

full_name = "   pritam kumar das   "
clean_name = full_name.strip()
name_parts = clean_name.split()
first_nam = name_parts[0].upper()
print(f"Hello, {first_nam}! Welcome.")






