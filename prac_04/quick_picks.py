import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

number_of_picks = int(input("How many quick picks? "))
for i in range(0, number_of_picks):
    quick_picks = []
    for j in range(0, 6):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in quick_picks:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_picks.append(number)
    quick_picks.sort()
    for j in range(0, len(quick_picks)):
        print(f"{quick_picks[j]:2}", end=" ")
    print()
