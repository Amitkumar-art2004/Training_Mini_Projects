import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

print("Original Data")
print(df)

# Pass/Fail function
def check_status(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"



# Grade function
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"



# Add Status Column
df["Status"] = df["Marks"].apply(check_status)


# Add Grade Column
df["Grade"] = df["Marks"].apply(calculate_grade)



# Filter passed students
passed_students = df[
    df["Status"] == "Pass"
]


print("\nPassed Students")
print(passed_students)



# Sort by highest marks
df = df.sort_values(
    by="Marks",
    ascending=False
)



print("\nSorted Data")
print(df)



# Save cleaned data
df.to_csv(
    "cleaned_students.csv",
    index=False
)


print(
    "\nCleaned data exported successfully"
)
