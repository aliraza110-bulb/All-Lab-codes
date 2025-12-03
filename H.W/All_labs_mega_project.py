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
# GLOBAL DATA (Because no class)
# ---------------------------
students = []

# ---------------------------
# FUNCTIONS WITHOUT SELF
# ---------------------------
def add_student():
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

        avg = np.mean(np.array(marks))

        info = {"name": name, "roll": roll, "marks": marks, "avg": avg}
        students.append(info)

        print("Student Added!")

    except Exception as e:
        print("Error:", e)


def summary():
    if not students:
        print("No data found.")
        return

    df = pd.DataFrame(students)
    print("\nDataFrame:\n", df)

    print("\nClass Average:", df["avg"].mean())
    print("Total Students (recursive count):", recursive_count(len(students)))


def visualize():
    if not students:
        print("No data.")
        return

    df = pd.DataFrame(students)

    sns.barplot(data=df, x="name", y="avg")
    plt.title("Average Marks")
    plt.show()


# ---------------------------
# EXTRA CONCEPTS
# ---------------------------
def extra_concepts_demo():
    print("\n===== EXTRA CONCEPTS =====")

    nums = [3, 1, 2]
    nums.append(5)

    tup = (10, 20)

    st = {1, 2, 3}

    d = {"A": 1, "B": 2}
    d["C"] = 3

    print("List:", nums, "Tuple:", tup, "Set:", st, "Dict:", d)


# ---------------------------
# MAIN PROGRAM (NO CLASS)
# ---------------------------
while True:
    print("\n--- Student Analyzer Mini Project ---")
    print("1. Add Student")
    print("2. Summary")
    print("3. Visualize")
    print("4. Extra Concepts Demo")
    print("5. Exit")

    c = input("Enter choice: ")

    if c == "1":
        add_student()
    elif c == "2":
        summary()
    elif c == "3":
        visualize()
    elif c == "4":
        extra_concepts_demo()
    elif c == "5":
        break
    else:
        print("Invalid choice!")
