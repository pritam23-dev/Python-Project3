# ধাপ ১: List (লিস্ট)⬇️

# মনে রাখার নিয়ম
# এই methods গুলো list-কে নিজেই বদলে দেয়, কিছু ফেরত দেয় না (None দেয়):
# append(), insert(), extend(), remove(), sort(), reverse(), clear()
# তাই এগুলোকে print()-এর ভেতরে বা x = fruits.sort() এভাবে লিখো না। এতে x-এ None ঢুকে যাবে।
# আর pop() আলাদা, সে বাদ দেওয়া item-টা ফেরত দেয়, তাই print(fruits.pop()) ঠিকঠাক কাজ করবে।

# fruits = ["apple","banana","cherry","mango","litchi"]
# fruits2 = ["orange","lychee"]
# fruits.extend(fruits2)
# print(fruits)

# fruits = ["apple","banana","cherry","mango","litchi"]
# fruits.remove("banana")
# fruits.insert(1,"orange")
# print(fruits )

# fruits.sort()
# print(fruits)
#
# fruits.sort(reverse= True )
# print(fruits)

# fruits.reverse()
# print(fruits)

# num = [1,1,2,2,3,3,3,3,3,4,5]
# print(num.count(3))
# print(num.index(4))
# print(len(num))
# print(type(num))


# ধাপ ২: Tuple (টাপল)⬇️
# Tuple কী?
# তোমার জাতীয় পরিচয়পত্র (NID) বা জন্মনিবন্ধন সনদের কথা ভাবো।
# একবার ছাপা হয়ে গেলে ওতে লেখা নাম, জন্মতারিখ, বাবার নাম আর নিজে নিজে বদলায় না।
# বদলাতে চাইলে নতুন করে সনদ বানাতে হয়। immutable

# একটা বিশেষ নিয়ম: একটা item-এর Tuple
# শুধু একটা item থাকলে শেষে কমা (,) দিতে হবে:

# name = ("Pritam",)    # এটা Tuple
# Name = ("Pritam")     # এটা Tuple না , string
# print(type(name))
# print(type(Name))

# Tuple বদলানো যায় না, তাই এর methods মাত্র ২টা: count, index

#Unpacking: Tuple-এর ভেতর থেকে মান বের করা

# student = ("Pritam", 20, "Dhaka")
# # student = name, age, city
# name, age, city = student
# print(name)
# print(age)
# print(city)

# নিয়ম: = সবসময় ডান দিক থেকে বাঁ দিকে কাজ করে
# Python আগে ডান দিকটা পড়ে (মান খোঁজে), তারপর সেটা বাঁ দিকের নামে রেখে দেয়।
# Real life উদাহরণ: মা বললেন, "স্কুল ব্যাগে বই, খাতা, কলম ভরে নাও।
# " কিন্তু তোমার কাছে বই, খাতা, কলম কিছুই নেই। ব্যাগে ভরবে কী?
#😅ভরার জিনিসই নেই, তাই আটকে গেলে। এটাকে বলে Packing (অনেকগুলো জিনিস এক ব্যাগে ভরা)

# Real life উদাহরণ: তোমার ব্যাগে বই, খাতা, কলম আছে। বাড়ি এসে ব্যাগ খুলে তিনটা
# জিনিস টেবিলের তিন জায়গায় রাখলে। জিনিস আগে থেকেই ব্যাগে ছিল, তাই কোনো সমস্যা হয়নি।
# এটাকে বলে Unpacking (ব্যাগ খুলে জিনিস আলাদা করা)।

# bag = ("English_Book", "Math_Notebook", "Red_Pen")
# book, notebook, pen = bag
# print(book)
# print(notebook)
# print(pen)


# ধাপ ৩: Set (সেট) ⬇️
# Set কী?
#
# তোমার ক্লাসের উপস্থিতির খাতা কল্পনা করো। শিক্ষক জিজ্ঞেস করলেন, "আজ কে কে এসেছে?"
# একই ছাত্র দুইবার হাত তুললেও খাতায় তার নাম একবারই উঠবে। আর খাতায় নাম কোন ক্রমে লেখা হলো,
# তাতে কিছু আসে-যায় না, শুধু জানা দরকার কে আছে আর কে নেই।
# Python-এ এটাই Set। এর দুইটা বড় বৈশিষ্ট্য:
# Duplicate থাকে না: একই জিনিস দুইবার দিলেও একবারই থাকে
# ক্রম (order) নেই: Index নেই, তাই s[0] কাজ করে না

# Subset ও Superset
# a = {1, 2}
# b = {1, 2, 3, 4}
# print(a.issubset(b))      # True (a পুরোটাই b-এর ভেতরে)
# print(b.issuperset(a))    # True
# print(a.isdisjoint({7, 8}))   # True (কোনো মিল নেই)

# fruits = {"apple","banana","mango","apple","banana"}
# print(fruits)
#
# # # Set-এর Methods
# # # ১. add(): একটা জিনিস যোগ
# # fruits.add("orange")
# # fruits.add("apple")    # আগে থেকেই আছে, তাই কিছু বদলাবে না
# # print(fruits)
# #
# # # ২. update(): একসাথে অনেকগুলো যোগ
# # fruits.update(["litchi","jackfruit"])
# # print(fruits)
#
# # ৩. remove(): বাদ দেওয়া (না থাকলে Error)
# fruits.remove("banana")
# # fruits.remove("grape")
# print(fruits)
#
# # ৪. discard(): বাদ দেওয়া (না থাকলে Error দেয় না)
# fruits.discard("mango")
# fruits.discard("grape")
# print(fruits)

# fruits = {"apple","banana","mango","apple","banana"}
# print(fruits)
#
# # ৫. pop(): যেকোনো একটা এলোমেলোভাবে বাদ , alada vhabe output ana
# x = fruits.pop()  # pop()➡️method sob smy print er vitor/alada variable declare korte hoy.
# print(x)
#
# # ৬. clear(): সব মুছে ফেলা
# fruits.clear()
# print(fruits)

# # Set-এর আসল শক্তি: গণিতের মতো কাজ
# # দুইটা ক্লাবের কথা ভাবো:

# cricket = {"Rahim","Karim","Sumon","Pritam"}
# foorball = {"Karim","Jamal","Pritam","Babu"}
#
# # Union (|): দুই ক্লাব মিলিয়ে সবাই (কেউ বাদ নেই, duplicate নেই)
# print(cricket | foorball )   # /
# #print(cricket.union(foorball))
#
# # Intersection (&): যারা দুই ক্লাবেই আছে
# print(cricket & foorball )  # /
# #print(cricket.intersection(foorball))
#
# # Difference (-): শুধু cricket-এ আছে, football-এ নেই
# print(cricket - foorball ) # /
# #print(cricket.difference(foorball))
#
# # Symmetric Difference (^): যারা শুধু একটাতেই আছে, দুটোতে নয়
# print(cricket ^ foorball )
# # print(cricket.symmetric_difference(foorball ))

# # সবচেয়ে কাজের ট্রিক: List থেকে Duplicate সরানো
# marks = [80,90,80,80,70,90,100]
# unique = list(set(marks))
# print(unique)
#
# # 🤔 accha tumi bolle set use korbo jokhon
# # 2/odhik kichu theke mil omil ber korbo tokhon .
# # ei kaj ta ki list / tuple diye kora jay na ? 😇
#
# cricket = ["Rahim", "Karim", "Sumon", "Pritam"]
# football = ["Karim", "Jamal", "Pritam", "Babu"]
#
# # List দিয়ে (Loop লাগে)
# common = []
# for name in cricket :
#     if name in football :
#         common.append(name)
# print(common)
#
# # Set দিয়ে (এক লাইন)
# print(set(cricket) & set(football))


# ধাপ ৪: Dictionary (ডিকশনারি)
# Dictionary কী?
# তোমার ফোনের Contact list ভাবো। সেখানে তুমি নম্বর দিয়ে কাউকে খোঁজো না, নাম দিয়ে খোঁজো:
# নাম লিখলেই নম্বর চলে আসে। নামটা হলো Key, নম্বরটা হলো Value।

# student = {
#     "name": "Pritam",
#     "age": 20,
#     "city": "Madaripur"
# }
# print(student)
# print(student["name"])
# # print(student["phone"]) # Error
# print(student.get("phone")) # get() দিয়ে নিরাপদে পড়া
# print(student.get("phone","নেই"))  # নেই (নিজের ডিফল্ট মান)
#print(student.get("city","hh"))
#
# student["age"] = 21  # বদলানো
# student["phone"] = "01612345098"  # নতুন Key যোগ (না থাকলে যোগ হয়, থাকলে বদলায়)
# print(student)

# student = {
#     "name": "Pritam",
#     "age": 20,
#     "city": "Madaripur"
# }
# # stu_inf = {
# #     "Old_city": "Dhaka",
# #     "blood": "O+"
# # }
# # print(student )
# # print(student.items())
# # print(student.keys())
# # print(student.values())
# # #student.update(stu_inf )
# # student.update({"Old_city": "Dhaka","blood": "O+"})
# # print(student)
#
# # print(student.pop("age"))
# # print(student.popitem())
#
# # del student["name"]
# # print(student)
#
# # student.clear()
# # print(student)
#
# print(student.copy())
#
# # ৯. setdefault(): Key না থাকলে বসাও, থাকলে যা আছে তাই দাও
# student.setdefault("country","Bangladesh")
# print(student)
#
# student.setdefault("country","Idia")   # output no cng becs country already here
# print(student)

# Loop দিয়ে ঘোরানো

# for key in student:
#     print(key)                      # শুধু Key
# for value in student.values():
#     print(value)                    # শুধু Value
# for key, value in student.items():
#     print(key, "→", value)          # দুটোই (সবচেয়ে বেশি ব্যবহার হয়)

# price = {
#     "চাল": 70,
#     "ডাল": 130,
#     "তেল": 180
# }
#
# price["চিনি"] = 120      # নতুন পণ্য
# price["চাল"] = 75        # দাম বদল
# total = 0
# for item, taka in price.items() :
#     print(item, ":",taka,"টাকা")
#     total += taka
#     #print(total)
# print("মোট:",total)

# text = ["a", "b", "a"]
# count = {}
#
# for ch in text:
#     print("এখন দেখছি:", ch, "| আগের সংখ্যা:", count.get(ch, 0))
#     count[ch] = count.get(ch, 0) + 1
#     print("খাতা:", count)
#     print("---")

# text = ["apple", "banana", "apple", "mango", "banana", "apple"]
#
# count= {}
# for fruits in text :
#     count[fruits] = count.get(fruits,0) + 1
# print(count)


# ধাপ ৬: Nested Structures (একটার ভেতরে আরেকটা)

## ধরন ১: List-এর ভেতরে List
# marks = [
#     [80,90,70],
#     [60,85,95],
#     [75,88,70]
# ]
# print(marks[2][1])
# marks[0][1] = 100
# print(marks )
# marks[2].append(200)
# print(marks)

# marks = [
#     [80,90,70],
#     [60,85,95],
#     [75,88,70]
# ]
# for student in marks:
#     for number in student:
#         print(number, end=" ")
#     print()

## ধরন ৩: List-এর ভেতরে Dictionary

# students = [
#     {"name": "Rahim", "age": 20},
#     {"name": "Karim", "age": 21},
#     {"name": "Sumon", "age": 19}
# ]
# students.append({"name": "Babu", "age": 22})
# for s in students:
#     print(s["name"],"-",s["age"],"বছর")

# ধরন ৪: Dictionary-র ভেতরে Dictionary

# contacts = {
#     "Rahim": {"phone": "01711111111", "email": "rahim@mail.com"},
#     "Karim": {"phone": "01822222222", "email": "karim@mail.com"}
# }
# print(contacts["Rahim"]["phone"])
# contacts["Karim"]["email"] = "K@mail.com"
# print(contacts)
# print(contacts["Karim"]["email"])
# contacts["Abir"] = {"phone": "01634546789", "email": "abir@mail.com"}
# print(contacts)

# # লক্ষ্য: Karim-এর ২য় নম্বর (85) বের করা।
# data = {
#     "class": "Ten",
#     "students": [
#         {"name": "Rahim", "marks": [80,90]},
#         {"name": "Karim", "marks": [70,85]}
#     ]
# }
# print(data["students"][1]["marks"][1])

a = [[1,2],[3,4]]
# b = a.copy()
# b[0][1] = 7
# print(b)
# print(a)  # 🤔 a bodlalo kno ?  solution ⬇️

# import copy
#
# b = copy.deepcopy(a)
# b[0][1] = 7
# print(b)
# print(a)

# practice

# school = {
#     "name": "Madaripur High School",
#     "teachers": ["Rahim sir", "Karim sir"],
#     "students": [
#         {"name": "Pritam", "marks": [80,90,85]},
#         {"name": "Babu", "marks": [70,75,60]}
#     ]
# }
# # print(school["name"])  # 1
# # print(school["teachers"][1])  # 2
# # print(school["students"][0]["marks"][1])    #3
# # school["students"].append({"name": "Sumon", "marks": [88, 92, 79]})
# # print(school)     #6
# # for s in school["students"]:
# #     print(s["name"])   # 5
# # print(sum(school["students"][1]["marks"])) # 4
#
# for s in school["students"]:
#     if s["name"] == "Babu":
#         print(sum(s["marks"]))
#
# for x in school["students"]:
#     if x["name"] == "Babu":
#         total = 0
#         for y in x["marks"]:
#             total += y
# print("Babu এর মোট মার্কস =",total )

# school = {
#     "name": "Madaripur High School",
#     "teachers": ["Rahim sir", "Karim sir"],
#     "students": [
#         {"name": "Pritam", "marks": [80,90,85]},
#         {"name": "Babu", "marks": [70,75,60]},
#         {"name": "Sumon", "marks": [88, 92, 79]}
#     ]
# }
# for s in school["students"]:
#     #print(s["name"],sum(s["marks"]))
#     print(f"{s['name']} এর মোট নম্বর: {sum(s['marks'])}")

# Tasks

library = {
    "name": "Madaripur Library",
    "books": [
        {"title": "Python Basics", "author": "Rahim", "price": 350, "tags": ["python", "coding"]},
        {"title": "Learn English", "author": "Karim", "price": 200, "tags": ["english", "language"]},
        {"title": "Data Science", "author": "Rahim", "price": 500, "tags": ["python", "data"]},
        {"title": "Web Design", "author": "Sumon", "price": 300, "tags": ["web", "coding"]}
    ]
}

print(library["name"])              # 1
print(library["books"][1]["title"])   # 2
for b in library["books"]:
    print(b["title"])           # 3

total = 0
for b in library["books"]:
    total += b["price"]
print(total)                    # 4

for b in library["books"]:
    if b["price"] <= 300 :
        continue
    print(b["title"])           # 5

# author = []
# for b in library["books"]:
#     author.append(b["author"])
# print(author)

authors = set()
for b in library["books"]:
    authors.add(b["author"])
print(authors)                  # 7


count = {}
for b in library["books"]:
    count[b["author"]] = count.get(b["author"], 0) +1
print(count)                    # 8

tags = set()
for b in library["books"]:
    for t in b["tags"]:
        tags.add(t)
print(tags)               # 9

# tags = set()
# for b in library["books"]:
#     tags.update(b["tags"])
# print(tags)                   # 9

max_price = 0
max_title = ""
for b in library["books"]:
    if b["price"] > max_price:
        max_price = b["price"]
        max_title = b["title"]
print(max_title , max_price )       # 10

first = library["books"][0]
max_price = first["price"]
max_title = first["title"]
for b in library["books"]:
    if b["price"] > max_price:
        max_price = b["price"]
        max_title = b["title"]
print(max_title , max_price )       # /10

first = library["books"][0]
low_price = first["price"]
low_title = first["title"]
for b in library["books"]:
    if b["price"] < low_price :
        low_price = b["price"]
        low_title = b["title"]
print(low_title , low_price )

library["books"].append({"title": "My book", "author":"Pritam", "price": 250, "tags": ["python","beginner"]})
print(len(library["books"]))

import os
os.remove("hisab.txt")

