import csv

class Student:
    # Valid grades
    __valid_grades = ['A', 'B', 'C', 'D', 'F']

    def __init__(self, student_id, name, course, grade):
        self.__student_id = student_id
        self.__name = name
        self.__course = course
        self.__grade = self.validate_grade(grade)

    # Private method to validate grade
    def validate_grade(self, grade):
        grade = grade.upper()
        if grade in Student.__valid_grades:
            return grade
        else:
            print(f"Invalid grade '{grade}' entered. Setting grade to 'Invalid'.")
            return "Invalid"

    # Public method to get student data
    def get_data(self):
        return {
            "ID": self.__student_id,
            "Name": self.__name,
            "Course": self.__course,
            "Grade": self.__grade
        }

class StudentManager:
    def __init__(self, filename="student_grade.csv"):
        self.filename = filename

    # Add a student record to CSV
    def add_student(self, student):
        data = student.get_data()
        try:
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data.keys())
                # Write header if file is empty
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(data)
            print(f"Student {data['Name']} added successfully.")
        except Exception as e:
            print("Error writing to file:", e)

    # Read and display all student records
    def view_students(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                print("\n--- All Student Records ---")
                for row in reader:
                    print(f"ID: {row['ID']}, Name: {row['Name']}, Course: {row['Course']}, Grade: {row['Grade']}")
        except FileNotFoundError:
            print("No student records found. File does not exist.")
        except Exception as e:
            print("Error reading file:", e)


# --- Example usage ---
manager = StudentManager()

while True:
    print("\n1. Add Student\n2. View All Students\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        grade = input("Enter Grade (A/B/C/D/F): ")
        student = Student(sid, name, course, grade)
        manager.add_student(student)
    elif choice == "2":
        manager.view_students()
    elif choice == "3":
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")
