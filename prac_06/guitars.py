from prac_06.guitar import Guitar


def main():
    print("My Guitars!")
    guitars = []

    name = get_input("Name: ")
    while name:
        year = get_input("Year: ")
        cost = get_input("Cost: ")
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added")
        name = get_input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars: ")
    counter = 1
    for guitar in guitars:
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {counter}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
        counter += 1


def get_input(prompt):
    if prompt == "Name: ":
        data = input(prompt)
    elif prompt == "Year: ":
        data = int(input(prompt))
    else:
        data = float(input(prompt))
    return data


if __name__ == '__main__':
    main()
