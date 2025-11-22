# Original book inventory
books = {
    "The Great Gatsby": 15.99,
    "To Kill a Mockingbird": 12.49,
    "1984": 10.99,
    "Pride and Prejudice": 9.99,
    "Moby Dick": 8.99
}

# 1️⃣ Create a backup copy
books_backup = books.copy()  # Shallow copy is enough for this dictionary

# 2️⃣ Print all book titles and their prices
print("Current Inventory:")
for title, price in books.items():
    print(f"{title}: ${price:.2f}")

# 3️⃣ Calculate total value of all books
total_value = sum(books.values())
print(f"\nTotal value of all books: ${total_value:.2f}")

# 4️⃣ Remove "1984" after it is sold
sold_book = "1984"
if sold_book in books:
    sold_price = books.pop(sold_book)
    print(f"\n'{sold_book}' sold for ${sold_price:.2f} and removed from inventory.")
else:
    print(f"\n'{sold_book}' is not in the inventory.")

# 5️⃣ Print updated inventory
print("\nUpdated Inventory:")
for title, price in books.items():
    print(f"{title}: ${price:.2f}")

# Optional: Show backup to confirm it remains unchanged
print("\nBackup Inventory (unchanged):")
for title, price in books_backup.items():
    print(f"{title}: ${price:.2f}")
