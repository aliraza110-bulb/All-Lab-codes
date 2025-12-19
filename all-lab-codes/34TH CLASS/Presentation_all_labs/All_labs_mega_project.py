import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

name_pattern = r"^[A-Za-z ]+$"
roll_pattern = r"^\d{2}[A-Za-z]{2}-\d{3}$"

def valid_name(name):
    return re.match(name_pattern, name)

def valid_roll(roll):
    return re.match(roll_pattern, roll)

def recursive_count_above_avg(students, avg):
    if not students:
        return 0
    return (1 if students[0]['avg'] > avg else 0) + recursive_count_above_avg(students[1:], avg)

students = []

def add_student():
    try:
        name = input("Enter Name: ").strip().title()
        if not valid_name(name):
            print("Invalid Name!")
            return

        roll = input("Enter Roll (e.g., 23CS-101): ").strip().upper()
        if not valid_roll(roll):
            print("Invalid Roll!")
            return

        marks = list(map(int, input("Enter Marks (comma separated): ").split(",")))
        avg = np.mean(marks)

        student = {"name": name, "roll": roll, "marks": marks, "avg": avg}
        students.append(student)
        print("Student added successfully!")

    except Exception as e:
        print("Error:", e)

def show_students():
    if not students:
        print("No students added.")
        return

    df = pd.DataFrame(students)
    print("\nSTUDENT DATAFRAME")
    print(df)

def report_card():
    if not students:
        print("No students added.")
        return

    roll = input("Enter Roll Number for Report Card: ").strip().upper()
    student = next((s for s in students if s['roll'] == roll), None)
    if not student:
        print("Student not found!")
        return

    total = sum(student['marks'])
    avg = student['avg']
    grade = "A" if avg >= 85 else "B" if avg >= 70 else "C" if avg >= 50 else "F"
    remarks = "Excellent" if grade=="A" else "Good" if grade=="B" else "Average" if grade=="C" else "Fail"

    print("\nREPORT CARD")
    print(f"Name: {student['name']}")
    print(f"Roll: {student['roll']}")
    print(f"Marks: {', '.join(map(str, student['marks']))}")
    print(f"Total: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Remarks: {remarks}")

def analyze_students():
    if not students:
        print("No students added.")
        return

    df = pd.DataFrame(students)
    print("\nSTUDENT STATISTICS")
    print(df.describe())

    plt.figure(figsize=(6,4))
    sns.barplot(x=df['name'], y=df['avg'])
    plt.title("Average Marks of Students")
    plt.show()

def save_students():
    if not students:
        print("No students to save.")
        return
    df = pd.DataFrame(students)
    df.to_csv("students_database.csv", index=False)
    print("Students saved to 'students_database.csv'")

def load_students():
    global students
    try:
        df = pd.read_csv("students_database.csv")
        students = df.to_dict("records")
        for s in students:
            if isinstance(s['marks'], str):
                s['marks'] = list(map(int, s['marks'].strip('[]').split(',')))
        print("Students loaded from 'students_database.csv'")
    except:
        print("No saved file found.")

def syllabus_coverage():
    coverage = {
        "Regex Validation": "validates names & roll numbers using regular expressions",
        "Recursion": "recursive function counts students above average",
        "Lists ": "stores student info inside a list",
        "Functions": "modular design with add_student, report_card, analyze_students etc.",
        "String Methods": "title(), upper(), join(), formatting report cards",
        "Conditional Statements": "grading system and menu selection",
        "Loops": "While loop menu and input loops",
        "NumPy & Pandas": "average calculations and data frames",
        "Matplotlib & Seaborn": "barplot visualizations of average marks",
        "Report Cards": "Professional formatting with grades & remarks",
        "File Handling": "save/load student database as CSV"
    }
    print("\nSYLLABUS COVERAGE")
    for topic, explanation in coverage.items():
        print(f"{topic}: {explanation}")

while True:
    print("""
MEGA STUDENT ANALYZER
1. Add Student
2. Show Students
3. Generate Report Card
4. Analyze Students (Graphs & Stats)
5. Save Students
6. Load Students
7. Syllabus Coverage
8. Exit
""")
    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        report_card()
    elif choice == "4":
        analyze_students()
    elif choice == "5":
        save_students()
    elif choice == "6":
        load_students()
    elif choice == "7":
        syllabus_coverage()
    elif choice == "8":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid option.")
