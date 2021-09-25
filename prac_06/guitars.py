from prac_06.guitar import Guitar


def main():
    print("My Guitars!")
    guitars = []

    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added")
        name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars: ")
    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
    # counter = 1
    # for guitar in guitars:
    #     if guitar.is_vintage():
    #         vintage_string = "(vintage)"
    #     else:
    #         vintage_string = ""
    #     print(f"Guitar {counter}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
    #     counter += 1


if __name__ == '__main__':
    main()
