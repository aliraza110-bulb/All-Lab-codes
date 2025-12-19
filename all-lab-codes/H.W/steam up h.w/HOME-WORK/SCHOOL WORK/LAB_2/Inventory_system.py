inventory = {}

while True:
    item = input("Enter item name (or 'stop' to finish): ")
    if item.lower() == "stop":
        break
    quantity = int(input("Enter quantity: "))
    inventory[item] = quantity

print("\nInventory List:")
for name in inventory:
    print(name, "-", inventory[name])
