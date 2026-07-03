class Student:
    def __init__(self,roll_no, name,age,marks):
        self.details = (roll_no, name,age)
        self.marks = marks
    def total_marks(self):
        return sum(self.marks.values())
    def average_marks(self):
        return self.total_marks() / len(self.marks)
    def calculate_grade(self):
        avg = self.average_marks()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"
class ResultSystem:
    def __init__(self):
        self.students = []
    def add_student(self,student):
        self.students.append(student)
    def generate_rank_list(self):
        return sorted(self.students,key=lambda student: student.total_marks(),reverse= True)
    def display_grade_report(self):
        print("+---------------------------------------------------+")
        print("|                   GRADE REPORT                    |")            
        print("+---------------------------------------------------+")
        for student in self.students:
            print( f"Roll No: {student.details[0]}, "
                f"Name: {student.details[1]}, "
                f"Grade: {student.calculate_grade()}"
            )
    
    def save_results(self):
        with open("results.txt","w") as file:
            for student in self.students:
                file.write(
                    f"Roll No: {student.details[0]}, "
                    f"Name: {student.details[1]}, "
                    f"Total: {student.total_marks()}, "
                    f"Average: {student.average_marks():.2f}, "
                    f"Grade: {student.calculate_grade()}\n"
                )
                
system = ResultSystem()
print("+-------------------------------------- ----------------------- ---+")
print("|          YOUR WELCOME IN EXAM RESULT PROCESSING SYSTEM           |")            
print("+------------------------------------------------------------------+")
print("\n")
s1 = Student(101,"Amit",20,{"Math":70 , "Python":80, "Physics":60})
s2 = Student(102,"Anish",21,{"Math":75, "Python":76, "Physics":50})
s3 = Student(103,"Aditya",21,{"Math":76, "Python":54,"Physics":76})
system.add_student(s1)
system.add_student(s2)
system.add_student(s3)
print("+---------------------------------------------------+")
print("|                     RANK LIST                     |")            
print("+---------------------------------------------------+")
rank_list = system.generate_rank_list()
for rank, student in enumerate(rank_list, start=1):
    print(
        f"Rank {rank}: {student.details[1]} "
        f"(Total Marks = {student.total_marks()})"
    )
system.display_grade_report()
system.save_results()
print("\nResults saved successfully in results.txt")
    
    
    
