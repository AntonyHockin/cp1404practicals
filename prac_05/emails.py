def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = strip_name_from_email(email)
        confirm = input(f"Is you name {name}? (Y/n)")
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email}) ")


def strip_name_from_email(email):
    prefix = email.split('@')[0]
    name_parts = prefix.split(".")
    name = " ".join(name_parts).title()
    return name


if __name__ == '__main__':
    main()
