from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0
    print("Let's drive")
    print("q)uit, c)hoose, d)rive")
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif choice == "d":
            print("Drive")
            # print(current_taxi)
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid input")
        print(f"Bill to date: ${total_bill}")
        print("q)uit, c)hoose, d)rive")
        choice = input(">>>").lower()
    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(current_taxi, total_bill):
    if current_taxi is not None:
        distance = int(input("Drive how far? "))
        current_taxi.drive(distance)
        print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare()}")
        total_bill += current_taxi.get_fare()
    else:
        print("Please select a taxi")
    return total_bill


def display_taxis(taxis):
    print("Available taxis:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
