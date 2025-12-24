students_scores = {
    "kamran": [85, 92, 78],
    "asif": [79, 95, 88],
    "abrar": [92, 90, 85],
    "danyial": [70, 75, 80]
}

def calculate_averages(scores_dict):
    averages = {}
    for student in scores_dict:
        averages[student] = sum(scores_dict[student]) / len(scores_dict[student])
    return averages

averages = calculate_averages(students_scores)

top_student = max(averages, key=averages.get)
print(f"Top student: {top_student} with average score {averages[top_student]:.2f}")
