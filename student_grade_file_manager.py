import csv
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

with open("students.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Amit", 85])
    writer.writerow(["Rahul", 92])
    writer.writerow(["Rohan", 45])

print("Student data saved!")

try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        print(file.read())

        with open("result.csv", "w") as out:
            fieldnames = ["Name", "Marks", "Grade"]
            writer = csv.DictWriter(out, fieldnames=fieldnames)

            writer.writeheader()
            for row in reader:
                marks = int(row["Marks"])

                writer.writerow({
                    "Name": row["Name"],
                    "Marks": marks,
                    "Grade": get_grade(marks)
                })

    print("Result file created successfully!")

except FileNotFoundError:
    print("students.csv file not found!")
except ValueError:
    print("Invalid marks found in file!")
