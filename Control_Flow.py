# # ধাপ ১: if (যদি)
# balance = 150
# if balance >= 100: # পরের লাইনে ইনডেন্টেশন (৪টা স্পেস) দিয়ে লিখতে হয়। এটা না দিলে error আসবে
#     print("চা কিনতে পারবো!")
#
# # ধাপ ২: else (নাহলে)
# pocket = 20
# if pocket >= 30:
#     print("বাসে উঠবো!")
# else:
#     print("হেঁটে যেতে হবে!")
#
# number = 7
# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
#
# # ধাপ ৩: elif (না হলে যদি)
#
# marks = 74
# if marks >= 80:
#     print("Grade: A+")
# elif marks >= 70:
#     print("Grade: A")
# elif marks >= 60:
#     print("Grade: A-")
# else:
#     print("Grade: B বা তার নিচে")
#
# temp = 17
# if temp >=30:
#     print("Wear light clothes.")
# elif temp >=20:
#     print("Wear normal dress.")
# elif temp >= 10:
#     print("Wear a sweater.")
# else:
#     print("Wear a thick jacket.")

# # for loop ব্যবহার করি যখন আগে থেকে জানা থাকে কতবার বা কোন কোন জিনিসের উপর কাজ করতে হবে।
#
# for i in range(5):
#     print("Pritam")
# for i in range(5):
#     print(i)
#
# bajar = ["chal","dal","tel","peayaj"]
# for item in bajar:
#     print("kinte hobe:",item)
#
# # Real life example ৩: ১ থেকে ৫ পর্যন্ত নামতা (২ এর ঘর)।
# for i in range(1,6):
#     print("2 x", i, "=", 2 * i)
#
# for p in range(1,6):
#     print("3 x",p,"=",3 * p)
#
# for l in range(0,11,2):
#     print(l)
#
# # ধাপ ৫: while loop (যতক্ষণ শর্ত সত্য)
#
# glass = 0
# while glass < 6:
#     glass += 1
#     print("পানি ঢালা হলো, এখন গ্লাসে :",glass,"ভাগ" )
#
# print("গ্লাস ভরে গেছে!")
#
# # Real life example ২: ব্যাংকের টাকা প্রতি মাসে ১০০ করে জমানো, ৫০০ হলে থামা।
#
# savings = 0
# month = 0
# while savings < 1000:
#     savings += 200
#     month += 1
#     print("মাস",month,": জমা হলো ",savings )
#
# print("লক্ষ্য পূরণ!")
#
#
# n = 0
# while n < 5:
#     n += 1
#     print(n)

# ধাপ ৬: break, continue, pass

# (ক) break (থামিয়ে দাও)
pockets = ["রুমাল","টাকা","চাবি","ফোন","কলম"]
for item in pockets:
    print("দেখছি:",item)
    if item == "চাবি":
        print("চাবি পেয়ে গেছি! আর খুঁজব না!")
        break

# (খ) continue (এটা বাদ দাও, পরেরটায় যাও)
# Real life example: আম কিনতে গেছ। পচা আম বাদ দিয়ে ভালোগুলো তুলবে।

mangoes = ["ভালো","পচা","ভালো","পচা","ভালো"]

for mango in mangoes:
    if mango == "পচা":
        continue
    print("এই আমটা নিলাম:",mango)

# গ) pass (কিছু করো না)
# pass মানে "এখানে কিছুই করবে না।" এটা শুনতে অদ্ভুত, কিন্তু কাজের। Python-এ if, for,
# while এর ভেতরে কোড খালি রাখা যায় না, error আসে। তখন জায়গা ভরাতে pass লিখি।

age = 20
if age >= 18:
    pass
else:
    print("তুমি এখনো ছোট")


