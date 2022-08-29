scores = {
    "asif": 100,
    "ali": 90,
    "ahmed": 80,
    "zain": 70,
}

grades = {}
for i in scores:
    if scores[i] > 90:
        grades[i] = "A"
    elif scores[i] > 80:
        grades[i] = "B"
    elif scores[i] > 70:
        grades[i] = "C"
    elif scores[i] > 60:
        grades[i] = "D"
    else:
        grades[i] = "Fail"

print(grades)
