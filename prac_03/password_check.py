"""Password checker program"""
MINIMUM_LENGTH = 10


def main():
    """Runs other functions when required"""
    password = get_password()
    create_asterisks(password)


def create_asterisks(password):
    """Print asterisks based on the length of the password"""
    for i in range(0, len(password)):
        print('*', end="")


def get_password():
    """Get password from the user, checking it reaches the minimum required length"""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters")
        password = input("Enter password: ")
    return password


main()
