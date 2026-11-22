# Calculator 🟰🐍


# while True:
#     try:
#         userinput_1 = float(input("Enter 1st number: "))
#         break
#     except ValueError:
#         print("Please, enter an integer or floating number!")
#
# while True:
#     try:
#         userinput_2 = float(input("Enter 2nd number: "))
#         break
#     except ValueError :
#         print("Please, enter an integer or floating number!")
#
# while True:
#     operator = input("What operation do you want? [ +,-,*,/ ]: ")
#
#     if operator == "+":
#         print(f"{userinput_1} + {userinput_2} = {userinput_1 + userinput_2}")
#         break
#     elif operator == "-":
#         print(f"{userinput_1} - {userinput_2} = {userinput_1 - userinput_2}")
#         break
#     elif operator == "*":
#         print(f"{userinput_1} * {userinput_2} = {userinput_1 * userinput_2}")
#         break
#     elif operator == "/":
#         while userinput_2 == 0:
#             print("Division by zero is undefined.")
#             try:
#                 userinput_2 = float(input("Enter 2nd number again (not 0) "))
#             except ValueError:
#                 print("Please, enter an integer or floating number!")
#         print(f"{userinput_1} / {userinput_2} = {userinput_1 / userinput_2}")
#         break
#     else:
#         print("Invalid operator! Please enter on of + - * /")



# def get_number(prompt):
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print("Please, enter an integer or floating number!")
#
#
# def get_operator():
#     while True:
#         oper = input("What operation do you want? [ +,-,*,/ ]: ")
#         if oper in ("+", "-", "*", "/"):
#             return oper
#
#
# def calculate(a, b, op):
#     if op == "+":
#         return a + b
#     elif op == "-":
#         return a - b
#     elif op == "*":
#         return a * b
#     else:
#         return a / b
#
#
# num1 = get_number("Enter 1st number: ")
# operator = get_operator()
# num2 = get_number("Enter 2nd number: ")
#
# while operator == "/" and num2 == 0:
#     print("Division by zero is undefined.")
#     num2 = get_number("Enter 2nd number again (not 0): ")
#
# result = calculate(num1, num2, operator)
# print(f"{num1} {operator} {num2} = {result}")


# # Calculator 🐍
# # user এর কাছ থেকে নাম্বার নিব।
# def get_number(prompt):
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print("Please, enter an integer or floating number!")
#
#
# # user এর কাছ থেকে operator নিব।
# def get_operator():
#     while True:
#         oper = input("What operation do you want? [ +, -, *, /, %, **, // ]: ")
#         if oper in ("+", "-", "*", "/", "%", "**","//"):
#             return oper
#
#
# # calculation করা।
# def calculate(a, b, op):
#     if op == "+":
#         return a + b
#     elif op == "-":
#         return a - b
#     elif op == "*":
#         return a * b
#     elif op == "/":
#         return a / b
#     elif op == "%":
#         return a % b
#     elif op == "**":
#         return a ** b
#     else:
#         return a // b
#
# # শেষের কাজ
# num1 = get_number("Enter 1st number: ")
#
# # user ২ টি সংখ্যা calculate করার পর আবার calculate করতে চাইতে পারে
# # তাই শেষের function call গুলো while loop এর মধ্যে রাখলাম।
# while True:
#     print(f"Current result: {num1}")
#     operator = get_operator()
#     num2 = get_number("Enter next number: ")
#
#     while operator in ("%", "/", "//")  and num2 == 0:
#         print("Division by zero is undefined.")
#         num2 = get_number("Enter next number again (not 0): ")
#
#     result = calculate(num1, num2, operator)
#     print(f"{num1} {operator} {num2} = {result}")
#
#     again = input("Continue with this result? (y/n): ").lower()
#     if again != "y":
#         break
#     num1 = result



# Calculator 🐍

# # শুধু এই character গুলো allow করব, যাতে অন্য কোনো code* চালানো না যায়।
ALLOWED = set("0123456789.+-*/%() ")

# expression ঠিক আছে কিনা check করা।
def is_valid(expr):
    return expr != "" and all(ch in ALLOWED for ch in expr)


# পুরো expression এর হিসাব করা (BODMAS নিজে নিজেই মেনে চলবে)।
def calculate(expr):
    return eval(expr)


Result = None

print("Expression লিখো, যেমন: 2*3-2+6")
print("আগের result এর সাথে চালাতে operator দিয়ে শুরু করো, যেমন: *2/3")
print("বের হতে q লিখো।\n")

while True:
    if Result is not None:
        print(f"Current result: {Result}")

    expr = input("Enter expression: ").replace(" ", " ")

    if expr.lower() == "q":
        print("Goodbye")
        break

    if not is_valid(expr):
        print("Invalid input! শুধু সংখ্যা আর + - * / % ( ) ব্যবহার করো।")
        continue

    # operator দিয়ে শুরু হলে আগের result সামনে জুড়ে দাও।
    # bracket দিয়েছি যাতে negative result এও ঠিক কাজ করে।
    if Result is not None and expr[0] in "+-*/%":
        expr = f"({Result}){expr}"

    try:
        Result = calculate(expr)
    except ZeroDivisionError:
        print("Division by zero is undefined.")
        continue
    except (SyntaxError, TypeError):
        print("Expression টা ঠিক নেই, আবার লিখো।")

    print(f"{expr} = {Result}")



















