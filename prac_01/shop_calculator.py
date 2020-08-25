"""Shop Calculator"""
total_price = 0

items = int(input("Number of items: "))
while items <= 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
for item in range(items):
    price = float(input("Price of item: "))
    total_price = total_price + price

print(f"Total price for {items} items is ${total_price}")
