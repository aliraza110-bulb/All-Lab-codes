expenses = []

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. View Total\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append({"name": name, "amount": amount})
    elif choice == "2":
        if expenses:
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['name']} - ${expense['amount']:.2f}")
        else:
            print("No expenses recorded.")
    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total expenses: ${total:.2f}")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")
