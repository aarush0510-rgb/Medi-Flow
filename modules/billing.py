from modules.database import load_table, save_table
from tabulate import tabulate

# Generating Bill ID :

def generate_bill_id():

    bills = load_table("bills")

    if not bills:
        return "B1001"

    last_number = max(int(bid[1:]) for bid in bills.keys())
    return f"B{last_number + 1}"

# Generating a bill for an appointment :

def generate_bill():

    appointments = load_table("appointments")
    doctors = load_table("doctors")
    patients = load_table("patients")
    bills = load_table("bills")

    print("\n====== GENERATE BILL ======\n")

    appointment_id = input("Enter Appointment ID : ")

    appointment = appointments.get(appointment_id)

    if appointment is None:
        print("Appointment Not Found!")
        return

    if appointment["status"] == "Cancelled":
        print("Cannot Bill a Cancelled Appointment!")
        return

    # Check if a bill already exists for this appointment
    existing = [b for b in bills.values() if b.get("appointment_id") == appointment_id]
    if existing:
        print("Bill Already Exists for this Appointment!")
        print("Bill ID :", existing[0]["bill_id"])
        return

    patient_id = appointment["patient_id"]
    doctor_id = appointment["doctor_id"]

    doctor = doctors.get(doctor_id)
    patient = patients.get(patient_id)

    if doctor is None:
        print("Doctor Not Found! Cannot Generate Bill.")
        return

    amount = doctor["fee"]
    bill_id = generate_bill_id()

    bills[bill_id] = {
        "bill_id": bill_id,
        "appointment_id": appointment_id,
        "patient_id": patient_id,
        "amount": amount,
        "status": "Unpaid"
    }

    save_table("bills", bills)

    print("\nBill Generated Successfully!")
    print("Bill ID       :", bill_id)
    print("Patient       :", patient["name"] if patient else "Unknown")
    print("Doctor        :", doctor["name"])
    print("Amount Due    :", amount)

# Viewing a specific bill :

def view_bill():

    bills = load_table("bills")
    patients = load_table("patients")

    bill_id = input("Enter Bill ID : ")

    bill = bills.get(bill_id)

    if bill is None:
        print("Bill Not Found!")
        return

    patient_name = patients.get(bill["patient_id"], {}).get("name", "Unknown")

    print()
    print(tabulate(
        [[bill["bill_id"], patient_name, bill["amount"], bill["status"]]],
        headers=["Bill ID", "Patient", "Amount", "Status"],
        tablefmt="grid"
    ))

# Viewing all bills :

def view_all_bills():

    bills = load_table("bills")
    patients = load_table("patients")

    if not bills:
        print("No Bills Found!")
        return

    rows = []
    for b in bills.values():
        patient_name = patients.get(b["patient_id"], {}).get("name", "Unknown")
        rows.append([b["bill_id"], patient_name, b["amount"], b["status"]])

    print()
    print(tabulate(
        rows,
        headers=["Bill ID", "Patient", "Amount", "Status"],
        tablefmt="grid"
    ))

# Marking a bill as paid :

def pay_bill():

    bills = load_table("bills")

    bill_id = input("Enter Bill ID : ")

    bill = bills.get(bill_id)

    if bill is None:
        print("Bill Not Found!")
        return

    if bill["status"] == "Paid":
        print("Bill is already Paid.")
        return

    bill["status"] = "Paid"
    bills[bill_id] = bill

    save_table("bills", bills)

    print("Payment Recorded Successfully!")
    print("Bill ID :", bill_id, "is now Paid.")