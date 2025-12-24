questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}.")

print(f"\nYou scored {score} out of {len(questions)}")
