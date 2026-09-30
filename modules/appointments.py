from modules.database import load_table, save_table
from tabulate import tabulate
from datetime import datetime
from modules.doctors import list_doctors

# Generating Appointment ID :

def generate_appointment_id():

    appointments = load_table("appointments")

    if not appointments:
        return "A1001"

    last_number = max(int(aid[1:]) for aid in appointments.keys())
    return f"A{last_number + 1}"

# Generating Token Number (per doctor, per date) :

def generate_token(doctor_id, date):

    appointments = load_table("appointments")

    tokens_today = [
        a["token"] for a in appointments.values()
        if a["doctor_id"] == doctor_id and a["date"] == date
    ]

    if not tokens_today:
        return 1

    return max(tokens_today) + 1

# Booking an appointment :

def book_appointment():

    patients = load_table("patients")
    doctors = load_table("doctors")
    appointments = load_table("appointments")

    print("\n====== BOOK APPOINTMENT ======\n")

    patient_id = input("Enter Patient ID : ").upper()

    if patient_id not in patients:
        print("Patient Not Found! Please register the patient first.")
        return

    patient_name = patients[patient_id]["name"]

    print("Patient Name :", patient_name)

    print("\nAvailable Doctors:")
    list_doctors()

    doctor_id = input("\nEnter Doctor ID : ").upper()

    if doctor_id not in doctors:
        print("Doctor Not Found!")
        return

    while True:
        date = input("Enter Date (DD-MM-YYYY) : ")

        try:
            datetime.strptime(date, "%d-%m-%Y")
            break

        except ValueError:
            print("Invalid Date Format! Use DD-MM-YYYY.")

    while True:
        time = input("Enter Time (HH:MM)      : ")

        try:
            time = datetime.strptime(time, "%H:%M").strftime("%H:%M")
            break
        except ValueError:
            print("Invalid Time Format! Use HH:MM.")

    # Checking for double booking
    for appointment in appointments.values():

        if (appointment["doctor_id"] == doctor_id and
            appointment["date"] == date and
            appointment["time"] == time and
            appointment["status"] != "Cancelled"):

            print("\nDoctor is already booked at this date and time!")
            print("Please choose another time.")
            return

    appointment_id = generate_appointment_id()
    token = generate_token(doctor_id, date)

    appointments[appointment_id] = {
        "appointment_id": appointment_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time,
        "token": token,
        "status": "Scheduled"
    }

    save_table("appointments", appointments)

    print("\nAppointment Booked Successfully!")
    print("Appointment ID :", appointment_id)
    print("Token Number   :", token)
    print("Doctor         :", doctors[doctor_id]["name"])

# Viewing all appointments :

def view_appointments():

    appointments = load_table("appointments")
    patients = load_table("patients")
    doctors = load_table("doctors")

    if not appointments:
        print("No Appointments Found!")
        return

    rows = []
    for a in appointments.values():
        patient_name = patients.get(a["patient_id"], {}).get("name", "Unknown")
        doctor_name = doctors.get(a["doctor_id"], {}).get("name", "Unknown")

        rows.append([
            a["appointment_id"], patient_name, doctor_name,
            a["date"], a["time"], a["token"], a["status"]
        ])

    print()
    print(tabulate(
        rows,
        headers=["ID", "Patient", "Doctor", "Date", "Time", "Token", "Status"],
        tablefmt="grid"
    ))

# Viewing appointments for a specific patient :

def view_patient_appointments():

    appointments = load_table("appointments")
    doctors = load_table("doctors")

    pid = input("Enter Patient ID : ")

    matches = [a for a in appointments.values() if a["patient_id"] == pid]

    if not matches:
        print("No Appointments Found for this Patient!")
        return

    rows = []
    for a in matches:
        doctor_name = doctors.get(a["doctor_id"], {}).get("name", "Unknown")
        rows.append([
            a["appointment_id"], doctor_name, a["date"],
            a["time"], a["token"], a["status"]
        ])

    print()
    print(tabulate(
        rows,
        headers=["ID", "Doctor", "Date", "Time", "Token", "Status"],
        tablefmt="grid"
    ))

# Cancelling an appointment :

def cancel_appointment():

    appointments = load_table("appointments")

    aid = input("Enter Appointment ID : ")

    appointment = appointments.get(aid)

    if appointment is None:
        print("Appointment Not Found!")
        return

    if appointment["status"] == "Cancelled":
        print("Appointment is already Cancelled.")
        return

    appointment["status"] = "Cancelled"
    appointments[aid] = appointment

    save_table("appointments", appointments)

    print("Appointment Cancelled Successfully!")

