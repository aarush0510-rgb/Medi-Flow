from modules.database import load_table, save_table
from tabulate import tabulate

# Generating Doctor ID :

def generate_doctor_id():

    doctors = load_table("doctors")

    if not doctors:
        return "D101"

    last_number = max(int(did[1:]) for did in doctors.keys())
    return f"D{last_number + 1}"

# Listing all doctors :

def list_doctors():

    doctors = load_table("doctors")

    if not doctors:
        print("No Doctors Found!")
        return

    rows = [
        [d["doctor_id"], d["name"], d["department"], d["fee"]]
        for d in doctors.values()
    ]

    print()
    print(tabulate(
        rows,
        headers=["ID", "Name", "Department", "Fee"],
        tablefmt="grid"
    ))

# Adding a new doctor :

def add_doctor():

    doctors = load_table("doctors")

    doctor_id = generate_doctor_id()

    print("\n====== ADD DOCTOR ======\n")

    name = input("Enter Name       : ")
    department = input("Enter Department : ")

    while True:
        fee = input("Enter Fee        : ")
        if fee.isdigit():
            fee = int(fee)
            break
        print("Invalid Fee! Enter numbers only.")

    doctors[doctor_id] = {
        "doctor_id": doctor_id,
        "name": name,
        "department": department,
        "fee": fee
    }

    save_table("doctors", doctors)

    print("\nDoctor Added Successfully!")
    print("Doctor ID :", doctor_id)

# Searching a doctor :

def search_doctor():

    doctors = load_table("doctors")

    did = input("Enter Doctor ID : ")

    doctor = doctors.get(did)

    if doctor:
        print()
        print(tabulate(
            [[doctor["doctor_id"], doctor["name"], doctor["department"], doctor["fee"]]],
            headers=["ID", "Name", "Department", "Fee"],
            tablefmt="grid"
        ))
    else:
        print("Doctor Not Found!")

# Updating doctor info :

def update_doctor():

    doctors = load_table("doctors")

    did = input("Enter Doctor ID : ")

    doctor = doctors.get(did)

    if doctor is None:
        print("Doctor Not Found!")
        return

    print("\nLeave blank to keep old value.\n")

    name = input(f"Name ({doctor['name']}) : ") or doctor["name"]
    department = input(f"Department ({doctor['department']}) : ") or doctor["department"]
    fee = input(f"Fee ({doctor['fee']}) : ")

    fee = int(fee) if fee.isdigit() else doctor["fee"]

    doctors[did] = {
        "doctor_id": did,
        "name": name,
        "department": department,
        "fee": fee
    }

    save_table("doctors", doctors)

    print("Doctor Updated Successfully!")