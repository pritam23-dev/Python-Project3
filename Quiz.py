
# score = 0
#
# quiz = [
#     {"question": "বাংলাদেশের রাজধানী কোথায়?", "answer": "Dhaka"},
#     {"question": "কত সালে বাংলাদেশ স্বাধীনতা লাভ করে?", "answer": "in 1971"},
#     {"question": "বাংলাদেশের বিজয় দিবস কবে?", "answer": "16th December"},
#     {"question": "বাংলাদেশের শহীদ দিবস কবে?", "answer": "21st February"}
# ]
#
# for ask in quiz:
#     print(ask["question"])
#     user_answer = input("তোমার উত্তর: ").strip()
#
#     if user_answer == ask["answer"]:
#         print("সটিক!\n")
#         score += 1
#     else:
#         print(f"ভুল! সঠিক উত্তর: {ask["answer"]}\n")
#
# print(f"তোমার score: {score}/{len(quiz)}")


x = "hello"
print(x.split())



score = 0

BN_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")


def normalize(text):
    text = text.strip().lower().translate(BN_DIGITS)
    return " ".join(text.split())

quiz = [
    {"question": "বাংলাদেশের রাজধানী কোথায়?",
     "answers": ["ঢাকা", "dhaka"]},
    {"question": "কত সালে বাংলাদেশ স্বাধীনতা লাভ করে?",
     "answers": ["১৯৭১", "১৯৭১ সালে", "1971", "in 1971"]},
    {"question": "বাংলাদেশের বিজয় দিবস কবে?",
     "answers": ["১৬ই ডিসেম্বর", "১৬ ডিসেম্বর", "16th December", "16 December", "16 Dec", "16th Dec"]},
    {"question": "বাংলাদেশের শহীদ দিবস কবে?",
     "answers": ["২১শে ফেব্রুয়ারি", "২১ ফেব্রুয়ারি", "21st February", "21 February", "21st Feb", "21 Feb"]},
]

for ask in quiz:
    print(ask["question"])
    user_answer = normalize(input("তোমার উত্তর: "))
    accepted = [normalize(a) for a in ask["answers"]]

    if user_answer in accepted:
        print("সঠিক!\n")
        score += 1
    else:
        print(f"ভুল! সঠিক উত্তর: {ask["answers"][0]}")


print(f"তোমার score: {score}/{len(quiz)}")





