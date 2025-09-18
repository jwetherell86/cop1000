def letterGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

studentName = input("Please enter your name:\n")

grade1 = float(input("Enter Grade 1:"))
grade2 = float(input("Enter grade 2:"))
grade3 = float(input("Enter Grade 3:"))
grade4 = float(input("Enter Grade 4:"))
grade5 = float(input("Enter Grade 5:"))

grades = [grade1,grade2, grade3, grade4, grade5]
average = sum(grades) / 5
letter = letterGrade(average)

print("\n Student Report")
print("Name:",studentName)
print("Average:", average)
print("Letter Grade:", letter)

