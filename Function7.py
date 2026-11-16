# Function

def make_tea():
    print("পানি গরম করছি")
    print("চা পাতা দিচ্ছি")
    print("চা তৈরি!")
make_tea()

def alarm():  # define , alarm set !
    print("উঠে পড়ো! সকাল হয়ে গেছে।")
alarm()   # এখন call করলাম, তাই প্রিন্ট হবে  , # alarm ring !

# Parameter

def make_tea(type):    # # type হলো PARAMETER (খালি জায়গা)
    print(f"{type} তৈরি")
make_tea("দুধ চা")      # # "দুধ চা" হলো ARGUMENT (আসল মান)
make_tea("লাল চা")
make_tea("লেবু চা")

def add(a,b):
    print(f"{a} + {b} = {a + b}")
add(6,6)
add(12,12)

def greet_friend(name):
    print(f"Hello! {name} কেমন আছো?")
greet_friend("Siam")
greet_friend("Nirad")
greet_friend("Jibon")

def rectangle_area(length,width):
    print(length * width)
rectangle_area(5,4)
rectangle_area(10,6)

# return

def rectangle_area(length, width):
    return length * width
print(rectangle_area(7,2) )

def square(n):
    return n * n
x = square(5)
y = square(3)
print(x + y)

def calculate_bill(price, quantity):
    return price * quantity
a = calculate_bill(250,2)
b = calculate_bill(500,3)
print(a + b)

def is_adult(age):
    return age > 18
z = is_adult(20)
print(z)

def test():
    print("লাইন ১")
    return "শেষ"
    print("লাইন ২")   # এটা কখনো চলবে না!
result = test()
print(result)

def check_age(age):
    if age < 0 :
        return "বয়স ঋণাত্মক হতে পারে না"
    return "বয়স ঠিক আছে"
print(check_age(-5))
print(check_age(20))
# -5 দিলে প্রথম return-এই function শেষ, দ্বিতীয় লাইনে আর যায়ইনি।

### ধাপ ৫: Default Parameter, মানে মান না দিলে ডিফল্ট মান

# তুমি দোকানে গিয়ে শুধু বললে "একটা চা দাও"। দোকানদার জিজ্ঞেস করল না চিনি কতটুকু।
# সে ধরে নিল ২ চামচ চিনি (এটাই তার ডিফল্ট)।
# ডিফল্টওয়ালা parameter সবসময় শেষে বসে

def power(base, exponent=2):
    return base ** exponent
print(power(5,3))

def discount_price(price, discount=10):
    return price - price * discount / 100
print(discount_price(1000))

def introduce(name, city="ঢাকা"):
    print(f"I am {name}, I live in {city}")
introduce("pritam","Madaripur")

# ধাপ ৬: Keyword Arguments, মানে নাম ধরে ধরে মান পাঠানো

def introduce(name, age, city):
    print(f"আমি {name}, বয়স {age}, থাকি {city}-এ")
introduce("রহিম", 20, "ঢাকা") # v
introduce(name= "রহিম", age= 20, city= "ঢাকা")  # Keyword (নাম ধরে),parameter_name=মান লিখতে হয়:
introduce(city= "ঢাকা", name= "রহিম", age= 20)  # কিন্তু এবার ক্রম উল্টে দিলেও ঠিক কাজ করবে:


def make_tea(sugar=2, milk=True, ginger=False):
    print(f"চিনি: {sugar}, দুধ: {milk}, আদা: {ginger}")
make_tea(2,True ,False)  ##  hard
make_tea(ginger= True)   # Default parameter এর সাথে Keyword Arguments দিয়ে সোজা: # easy

def introduce(name, age=18, city="Madaripur"):
    print(name, age, city)
introduce("রহিম", age=20, city="ঢাকা")     # ⚠️ নিয়ম: Positional আগে, Keyword পরে  # ঠিক ✅
# introduce(name="রহিম", 20, "ঢাকা")  #   ভুল ❌ SyntaxError

def order_food(item, quantity=1, delivery=True):
    print(f"অর্ডার: {item}, পরিমাণ: {quantity}, ডেলিভারি: {delivery}")
order_food("Pizza")
order_food("Pizza",delivery=False)
order_food(delivery=False , quantity=2, item="Barger")

print("A", "B", "C", sep=" | ")

print("A", end=" ! ")
print("B", end=" ! ")
print("C")

# ধাপ ৭ (শেষ ধাপ): Scope, মানে Variable কোথায় কাজ করে
# 1. Local: function-এর ভেতরে বানানো variable
# 2. Global: function-এর বাইরে বানানো variable

#1. Local variable/scope
def my_room():
    secret = "আমার ডায়েরি"  # local variable
    print(secret )
my_room()

# global variable/scope
school = "মাদারীপুর সরকারি কলেজ"   # global variable
def show():
    print(f"আমি পড়ি {school}-এ")
show()
print(school)

# একই নামে local আর global থাকলে
x = 10
def test():
    x = 99
    print("ভেতরে:", x)
test()
print("বাইরে:", x)

count = 4
def add_one():
    global count
    count = count + 1
add_one()
add_one()
print(count)

def add_one(number):
    return number + 1
count = 4
count = add_one(count)
count = add_one(count)
print(count)
#দ্বিতীয় উপায়টা সাধারণত ভালো, কারণ function নিজে নিজের মধ্যে সীমাবদ্ধ থাকে,
# বাইরের কিছু গোপনে বদলায় না। বড় প্রজেক্টে global বেশি ব্যবহার করলে কোড বোঝা ও ভুল খোঁজা কঠিন হয়ে যায়।

balance = 1000
def withdraw_Global():
    global balance
    balance -= 10
withdraw_Global()
withdraw_Global()
print(balance)

def withdraw_return(amount):
    return amount - 10
balance = 1000
balance = withdraw_return(balance)
balance = withdraw_return(balance)
print(balance)

