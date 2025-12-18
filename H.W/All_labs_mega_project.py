import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# BASIC FUNCTIONS + RECURSION
# ---------------------------
def greet(name):
    return f"Hello, {name}!"

def recursive_count(n):
    if n == 0:
        return 0
    return 1 + recursive_count(n - 1)

# ---------------------------
# REGEX VALIDATION
# ---------------------------
def valid_name(name):
    return re.match(r"^[A-Za-z ]+$", name)

def valid_roll(roll):
    return re.match(r"^\d{2}[A-Za-z]{2}-\d{3}$", roll)

# ---------------------------
# MAIN CLASS
# ---------------------------
class StudentSystem:
    def __init__(self):
        self.students = []   # list

    def add_student(self):
        try:
            name = input("Enter name: ").strip().title()
            if not valid_name(name):
                print("Invalid name!")
                return

            roll = input("Enter roll (e.g., 23CS-101): ")
            if not valid_roll(roll):
                print("Invalid roll format!")
                return

            marks = list(map(int, input("Enter marks (comma separated): ").split(",")))

            avg = np.mean(np.array(marks))   # NUMPY USE
            info = {"name": name, "roll": roll, "marks": marks, "avg": avg}

            self.students.append(info)
            print("Student Added!")

        except Exception as e:
            print("Error:", e)

    def summary(self):
        if not self.students:
            print("No data found.")
            return

        df = pd.DataFrame(self.students)   # PANDAS USE
        print("\nDataFrame:\n", df)

        print("\nClass Average:", df["avg"].mean())
        print("Total Students (recursive count):", recursive_count(len(self.students)))

    def visualize(self):
        if not self.students:
            print("No data.")
            return

        df = pd.DataFrame(self.students)

        sns.barplot(data=df, x="name", y="avg")
        plt.title("Average Marks")
        plt.show()

# ---------------------------
# SUPPORTING CONCEPTS AREA
# (Covers lists, tuples, sets, dictionaries)
# ---------------------------
def extra_concepts_demo():
    print("\n===== EXTRA CONCEPTS =====")

    # List
    nums = [3, 1, 2]
    nums.append(5)

    # Tuple
    tup = (10, 20)

    # Set
    st = {1, 2, 2, 3}

    # Dictionary
    d = {"A": 1, "B": 2}
    d["C"] = 3

    print("List:", nums, "Tuple:", tup, "Set:", st, "Dict:", d)

# ---------------------------
# MAIN PROGRAM
# ---------------------------
system = StudentSystem()

while True:
    print("\n--- Student Analyzer Mini Project ---")
    print("1. Add Student")
    print("2. Summary")
    print("3. Visualize")
    print("4. Extra Concepts Demo")
    print("5. Exit")

    c = input("Enter choice: ")

    if c == "1":
        system.add_student()
    elif c == "2":
        system.summary()
    elif c == "3":
        system.visualize()
    elif c == "4":
        extra_concepts_demo()
    elif c == "5":
        break
    else:
        print("Invalid choice!")
