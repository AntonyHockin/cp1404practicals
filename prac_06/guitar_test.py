from prac_06.guitar import Guitar
CURRENT_YEAR = 2021

first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
second_guitar = Guitar("Another Guitar", 2018, 2)
print(f"{first_guitar.name} get_age() - Expected {99} Got {first_guitar.get_age()}")
print(f"{second_guitar.name} get_age() - Expected {3} Got {first_guitar.get_age()}")
print(f"{first_guitar.name} is_vintage() - Expected {True} Got {first_guitar.is_vintage()}")
print(f"{second_guitar.name} is_vintage() - Expected {False} Got {second_guitar.is_vintage()}")

# print(first_guitar.get_age())  # Expected 99 Got 99
# print(second_guitar.get_age())  # Expected 3 Got 3
# print(first_guitar.is_vintage())  # Expected True Got True
# print(second_guitar.is_vintage())  # Expected False Got False
