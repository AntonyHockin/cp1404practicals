total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 1:
    print("Invalid Number, number must be greater than 0")
    number_of_items = int(input("Number of items: "))
for i in range(0, number_of_items):
    price = float(input("Price of item: "))
    total_price += price
# print(total_price)
if total_price > 100:
    total_price = total_price - total_price * 0.1
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
