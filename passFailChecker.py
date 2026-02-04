grades = ["A", "A", "B", "U", "F", "E", "D"]
grade = []
for x in grades:
    if x == "A" or x == "B":
        x = True
        if x == True:
            grade.append("Pass")
    else:
        x = False
        grade.append("Fail")
print(grade)
