"""Password checker program"""
MINIMUM_LENGTH = 10

password = input("Enter password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password must be at least {MINIMUM_LENGTH} characters")
    password = input("Enter password: ")
for i in range(0, len(password)):
    print('*', end="")
