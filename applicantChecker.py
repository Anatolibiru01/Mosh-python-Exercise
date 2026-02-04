print("Welcome to the Applicant’s eligibility checker")

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
age = input("Please enter your age: ")
marks = float(input("Please enter your overall marks (out of 600): "))

mark = (marks * 0.166667)
# print(mark)

def checking_for_qualification(mark):
    if mark >= 80:
        print(f"{last_name}, You are eligible for both admission and scholarship")
        scholarship = input("  Are you seeking a scholarship? [Y/N]: ")
        if scholarship.lower() == "y":
            return f"Congratulations {last_name}! You are eligible for a scholarship! \n"
        elif scholarship.lower() == "n":
            pass
    elif 80 > mark >= 60:
        return f"{last_name}, You are only eligible for admission \n"
    else:
        return f"{last_name}, your point is not sufficient \n "


print(checking_for_qualification(mark))
print(f"Thank you for your input and we wish you good luck!")