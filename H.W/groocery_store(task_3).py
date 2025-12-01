# Task #3
# Scenario: 
# You are developing a dynamic inventory management system for a grocery store. The store manager wants to track and update the stock of fruits in real-time. Instead of starting with a predefined list of fruits, the manager will input fruit names one by one, and they will be added to the inventory.
# The manager also requires the following tasks:
# Ask the user to input fruit names and add them to the tuple one by one until the tuple reaches a length of 5.
# Once the tuple reaches the required length, update the tuple by removing a specific fruit that the manager no longer wants to stock, and then add a new fruit to the tuple.
# Ensure that the final updated tuple reflects the current state of the inventory.
# Task Description: 
# In this word problem, you are tasked with building a dynamic inventory management system for a grocery store where the manager inputs fruit names one by one to add them to a tuple. Once the tuple reaches a length of 5, you will update the tuple by removing a specific fruit and adding a new one. The final tuple will reflect the updated inventory.



inventory = ()

while len(inventory) < 5:
    fruit = input("Enter the name of fruit to add: ")
    inventory = inventory + (fruit,)
    print("Current inventory:", inventory)

print("\nFinal Inventory:", inventory)

inventory_list = list(inventory)

fruit_to_remove = input("\nEnter the fruit name to remove: ")
if fruit_to_remove in inventory_list:
    inventory_list.remove(fruit_to_remove)
    print(f"{fruit_to_remove} removed.")
else:
    print(f"{fruit_to_remove} not found in inventory!")

new_fruit = input("Enter the name of fruit to add: ")
inventory_list.append(new_fruit)

inventory = tuple(inventory_list)

print("\nUpdated Inventory:", inventory)
