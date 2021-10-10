from prac_08.unreliable_car import UnreliableCar

good_car = UnreliableCar("Slightly old camry", 50, 90)
bad_car = UnreliableCar("The rust bucket", 50, 10)

for i in range(1, 10):
    print(f"Attempting to drive {i}km")
    print(f"{good_car.name} drove {good_car.drive(i)}km")
    print(f"{bad_car.name} drove {bad_car.drive(i)}km")
    print()

print("End results")
print(good_car)
print(bad_car)