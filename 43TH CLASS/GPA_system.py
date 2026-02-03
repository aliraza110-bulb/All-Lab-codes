import numpy as np
import pandas as pd

marks = np.array([
    [85,78,90,88],
    [70,75,72,68],
    [92,95,94,96],
    [65,66,63,67],
    [88,84,86,90]
])

students = ["Ali","Sara","Jhon","Ayesha","Zain"]
subjects = ["Maths","Physics","Chemistry","English"]

df = pd.DataFrame(marks, index=students, columns=subjects)

# Total Marks
df["total"] = df.sum(axis=1)

# Percentage
df["percentage"] = (df["total"] / 400) * 100

# GPA (4 scale)
df["GPA"] = df["percentage"] / 25

# Grade using GPA
df["Grade"] = pd.cut(
    df["GPA"],
    bins=[0, 2, 3, 3.7, 4.01],   # bins must be increasing
    labels=["C", "B", "A", "A+"]
)

# Ranking
df["Rank"] = df["GPA"].rank(ascending=False, method="min").astype(int)

print(df)

print("\nTop Student:\n", df.loc[df["Rank"] == 1])


top3_subjectwise = {subject: df[subject].nlargest(3) for subject in subjects}

for subject, top in top3_subjectwise.items():
    print(f"\n📘 Top 3 in {subject}:\n{top}")