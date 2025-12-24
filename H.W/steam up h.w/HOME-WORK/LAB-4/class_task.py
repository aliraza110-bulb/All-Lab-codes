books = {
    "The Great Gatsby": 15.99,
    "To Kill a Mockingbird": 12.49,
    "1984": 10.99,
    "Pride and Prejudice": 9.99,
    "Moby Dick": 8.99
}

copy=books.copy()
print("The copy of books",books)

for title,prices in books:
    print("Title",title,"Prices",prices)