from modules.database import load_table


def hospital_summary():

    patients = load_table("patients")
    doctors = load_table("doctors")
    appointments = load_table("appointments")
    bills = load_table("bills")

    print("\n====== HOSPITAL SUMMARY ======")

    print("Total Patients :", len(patients))
    print("Total Doctors  :", len(doctors))
    print("Total Appointments :", len(appointments))
    print("Total Bills :", len(bills))

def patient_report():

    patients = load_table("patients")

    print("\n====== PATIENT REPORT ======")

    print("Total Patients :", len(patients))


def doctor_report():

    doctors = load_table("doctors")

    print("\n====== DOCTOR REPORT ======")

    print("Total Doctors :", len(doctors))


def appointment_report():

    appointments = load_table("appointments")

    print("\n----- APPOINTMENT REPORT -----")

    total_appointments = len(appointments)

    print(f"Total Appointments : {total_appointments}")

    completed = 0
    pending = 0
    cancelled = 0

    for appointment in appointments.values():

        status = appointment.get("status", "").lower()

        if status == "completed":
            completed += 1

        elif status == "pending":
            pending += 1

        elif status == "cancelled":
            cancelled += 1

    print(f"Completed          : {completed}")
    print(f"Pending            : {pending}")
    print(f"Cancelled          : {cancelled}")


def billing_report():

    bills = load_table("bills")

    print("\n----- BILLING REPORT -----")

    total_bills = len(bills)

    total_revenue = 0

    for bill in bills.values():

        amount = bill.get("amount", 0)

        try:
            total_revenue += float(amount)
        except:
            pass

    print(f"Total Bills        : {total_bills}")
    print(f"Total Revenue      : ₹{total_revenue:.2f}")