from modules.database import load_table, save_table
from tabulate import tabulate

# Generating Patient ID :

def generate_patient_id():

    patients = load_table("patients")

    if not patients:
        return "P1001"

    # Get the highest existing numeric suffix
    last_number = max(int(pid[1:]) for pid in patients.keys())
    return f"P{last_number + 1}"

# Registering a patient :

def register_patient():

    patients = load_table("patients")

    patient_id = generate_patient_id()

    print("\n====== REGISTER PATIENT ======\n")

    name = input("Enter Name   : ")
    age = int(input("Enter Age    : "))
    gender = input("Enter Gender : ")

    while True:
        phone = input("Enter Phone  : ")

        if len(phone) == 10 and phone.isdigit():
            break

        print("Invalid Phone Number! Enter 10 digits.")

    patients[patient_id] = {
        "patient_id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone
    }

    save_table("patients", patients)

    print("\nPatient Registered Successfully!")
    print("Patient ID :", patient_id)

# Search Patient

def search_patient():

    patients = load_table("patients")

    pid = input("Enter Patient ID : ")

    patient = patients.get(pid)

    if patient:
        print()
        print(tabulate(
            [[patient["patient_id"], patient["name"], patient["age"],
              patient["gender"], patient["phone"]]],
            headers=["ID", "Name", "Age", "Gender", "Phone"],
            tablefmt="grid"
        ))
    else:
        print("Patient Not Found!")

# Updating Patient Info

def update_patient():

    patients = load_table("patients")

    pid = input("Enter Patient ID : ")

    patient = patients.get(pid)

    if patient is None:
        print("Patient Not Found!")
        return

    print("\nLeave blank to keep old value.\n")

    name = input(f"Name ({patient['name']}) : ") or patient["name"]
    age = input(f"Age ({patient['age']}) : ")
    gender = input(f"Gender ({patient['gender']}) : ") or patient["gender"]
    phone = input(f"Phone ({patient['phone']}) : ") or patient["phone"]

    age = int(age) if age != "" else patient["age"]

    patients[pid] = {
        "patient_id": pid,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone
    }

    save_table("patients", patients)

    print("Patient Updated Successfully!")