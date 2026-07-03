
StudentManagementSystem = {}
n = int(input("Enter number of students: "))
for i in range(1, n + 1):
    name = input(f"\nEnter name of student {i}: ")
    math_marks = int(input("Enter Math marks: "))
    coa_marks = int(input("Enter COA marks: "))

    StudentManagementSystem[f"std{i}"] = {
        "name": name,
        "marksOfMath": math_marks,
        "marksOfCOA": coa_marks
    }
students = []
topper_name = ""
highest_average = 0
for student in StudentManagementSystem.values():
    name = student["name"]
    average = (student["marksOfMath"] + student["marksOfCOA"]) / 2
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    students.append([name, average, grade])
    if average > highest_average:
        highest_average = average
        topper_name = name
print("\nStudent Results:")
for student in students:
    print(student)
print("\nTopper:", topper_name)
print("Highest Average:", highest_average)
