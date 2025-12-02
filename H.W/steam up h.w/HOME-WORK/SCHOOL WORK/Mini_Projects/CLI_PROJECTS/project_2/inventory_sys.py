inventory = {}

while True:
    print("\n1. Add Item\n2. Update Item\n3. Remove Item\n4. View Inventory\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        inventory[item] = inventory.get(item, 0) + qty
    elif choice == "2":
        item = input("Enter item name to update: ")
        if item in inventory:
            qty = int(input("Enter new quantity: "))
            inventory[item] = qty
            print(f"{item} updated.")
        else:
            print("Item not found.")
    elif choice == "3":
        item = input("Enter item name to remove: ")
        if item in inventory:
            del inventory[item]
            print(f"{item} removed.")
        else:
            print("Item not found.")
    elif choice == "4":
        if inventory:
            for item, qty in inventory.items():
                print(f"{item} - {qty}")
        else:
            print("Inventory is empty.")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")
