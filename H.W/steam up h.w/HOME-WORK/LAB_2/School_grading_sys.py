num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    print(f"\nStudent #{i + 1}")
    name = input("Enter student name: ")
    score = float(input("Enter student score (out of 100): "))

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Name: {name:<10} | Score: {score:>5.1f} | Grade: {grade}")
