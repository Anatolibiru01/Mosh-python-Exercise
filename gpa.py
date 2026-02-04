Subjects = ["Applied math", "Physics",
            "Chemistry", "Python", "Civic", "C.English"]


def grade(point):
    if 85 <= point <= 100:
        return 4
    elif point >= 80:
        return 3.75
    elif point >= 75:
        return 3.5
    elif point >= 70:
        return 3
    elif point >= 65:
        return 2.75
    elif point >= 60:
        return 2.5
    elif point >= 50:
        return 2
    elif point >= 45:
        return 1.75
    elif point >= 40:
        return 1
    else:
        return 0


def grade_with_letter(gra):
    if 85 <= gra <= 100:
        return "A"
    elif gra >= 80:
        return "A-"
    elif gra >= 75:
        return "B+"
    elif gra >= 70:
        return "B"
    elif gra >= 65:
        return "B-"
    elif gra >= 60:
        return "C+"
    elif gra >= 50:
        return "C"
    elif gra >= 45:
        return "C-"
    elif gra >= 40:
        return "D"
    else:
        return "F"


def pass_or_fail(summery):
    if gpa_summery == 4:
        return "Congratulations!! Finished with great honour"
    elif 3.90 > gpa_summery > 2.00:
        return "Congratulations!! Passed!"
    elif 2.00 > gpa_summery > 1.50:
        return "Passed but improve it!"
    else:
        return "sorry Failed!"


score = []
for i in Subjects:
    while True:
        try:
            point = float(input(f"Enter {i} out of 100: "))
            if 0 <= point <= 100:
                print(f"    Your grade is: {grade_with_letter(point)}\n")
                score.append(point)
                break
            else:
                print("  error point enter 0-100")
        except:
            print("  error input! enter again")


tmp = []
for i in score:
    tmp.append(grade(i))

gpa_summery = (tmp[0]*4 + 3*(tmp[1] + tmp[2] + tmp[3] + tmp[4] + tmp[5]))/19

print(f"  Your GPA is: {round(gpa_summery, 2)} \n{pass_or_fail(gpa_summery)}")
