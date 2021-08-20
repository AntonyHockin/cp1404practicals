"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#         print("Excellent")
# if score < 50:
#     print("Bad")


def main():
    score = float(input("Enter score: "))
    result = calculate_result(score)
    print(result)
    random_score = random.randint(0, 100)
    print(f"Random score is {random_score}")
    result = calculate_result(random_score)
    print(result)


def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Pass"
        else:
            return "Bad"


main()
