students = {}

while True:
    print("\n1. Add Student\n2. Remove Student\n3. View All Students\n4. Find Top Scorer\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))
        students[name] = score
    elif choice == "2":
        name = input("Enter student name to remove: ")
        if name in students:
            del students[name]
            print(f"{name} removed.")
        else:
            print("Student not found.")
    elif choice == "3":
        if students:
            for name, score in students.items():
                print(f"{name} - {score}")
        else:
            print("No students found.")
    elif choice == "4":
        if students:
            top_student = max(students, key=students.get)
            print(f"Top student: {top_student} with score {students[top_student]}")
        else:
            print("No students found.")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")
