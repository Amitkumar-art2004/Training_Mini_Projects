class Patient:
    def __init__(self,patient_id,name,age):
        if age <= 0:
            raise ValueError("Age must be greater than 0")
        self.patient_id = patient_id
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.patient_id},{self.name},{self.age}"
class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
    def __str__(self):
        return f"{self.doctor_id},{self.name},{self.specialization}"
class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}
        self.appointments = []
    def add_patient(self,patient):
        self.patients[patient.patient_id] = patient
    def schedule_appointment(self,patient_id,doctor):
        if patient_id not in self.patients:
            raise Exception("patient ID not found")
        appointment = {
            "patient" : self.patients[patient_id].name,
            "doctor" : doctor.name
        }
        self.appointments.append(appointment)
    def save_records(self):
        with open("patients.txt","w") as file:
            for patient in self.patients.values():
                file.write(str(patient)+"\n")
        with open("appointments.txt", "w") as file:
            for app in self.appointments:
                file.write(f"Patient:{app['patient']},Doctor:{app['doctor']}\n")
try:
    hms = HospitalManagementSystem()
    print("+---------------------------------------------------+")
    print("|           Hospital Management System              |")            
    print("+---------------------------------------------------+")
    p1ID = int(input("Enter first patient DI : "))
    p1Name = input("Enter first patient name : ")
    p1Age = int(input("Enter first patient age : "))
    p1 = Patient(p1ID,p1Name,p1Age)
    print("\n")
    p2ID = int(input("Enter second patient DI : "))
    p2Name = input("Enter second patient name : ")
    p2Age = int(input("Enter second patient age : "))
    p2 = Patient(p2ID,p2Name,p2Age)
    print("\n")
    print("+---------------------------------------------------+")
    print("|              SCHEDULED APPOINTMENT                |")            
    print("+---------------------------------------------------+")

    d1 = Doctor(1,"Dr. Gulati","Cardiologist")
    d2 = Doctor(1,"Dr. Murli","Cardiologist")
    hms.add_patient(p1)
    hms.add_patient(p2)
    hms.schedule_appointment(p1ID,d1)
    hms.schedule_appointment(p2ID,d2)
    hms.save_records()
    with open("appointments.txt", "r") as file:
        print(file.read())
    print("+---------------------------------------------------+")
    print("|                 SAVED INFORMATION                 |")            
    print("+---------------------------------------------------+")    
    with open("patients.txt" ,"r") as file:
        print(file.read())
except ValueError as e:
    print("Invalid Patient Information : ",e)
