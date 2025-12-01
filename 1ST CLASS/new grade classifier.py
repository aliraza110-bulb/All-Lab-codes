def grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50: 
        return "E"
    else:
       return "fail"

n = int(input("Input The Students number  "))
results = []
for i in range(1, n + 1):
    name = input(f"student {i} name:") or f"students{i}"
    s= int(input ((f"{name}'score (0-100):")))
    results.append((name, s, grade(s)))

print("\nResults")
print("." * 28)
for name, s, g in results:
    print(f"name {name:12}| score: {s:3d} | Grade: {g}")