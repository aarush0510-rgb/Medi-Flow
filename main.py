from modules.database import setup_database
from modules.auth import setup_auth, register_user, login
from modules.patients import register_patient, search_patient, update_patient
from modules.doctors import list_doctors
from modules.appointments import book_appointment, view_appointments, cancel_appointment
from modules.billing import generate_bill, view_bill
from modules.reports import hospital_summary, patient_report, doctor_report, billing_report, appointment_report


def patient_menu():
    while True:
        print("\n====== PATIENT MENU ======")
        print("1. Register Patient")
        print("2. Search Patient")
        print("3. Update Patient")
        print("4. Back to Main Menu")
        choice = input("Enter Choice : ")

        if choice == "1":
            register_patient()
        elif choice == "2":
            search_patient()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            break
        else:
            print("Invalid Choice")


def doctor_menu():
    while True:
        print("\n====== DOCTOR MENU ======")
        print("1. List Doctors")
        print("2. Back to Main Menu")

        choice = input("Enter Choice : ")

        if choice == "1":
            list_doctors()
        elif choice == "2":
            break
        else:
            print("Invalid Choice")


def appointment_menu():
    while True:
        print("\n====== APPOINTMENT MENU ======")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Cancel Appointment")
        print("4. Back to Main Menu")

        choice = input("Enter Choice : ")

        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            cancel_appointment()
        elif choice == "4":
            break
        else:
            print("Invalid Choice")


def billing_menu():
    while True:
        print("\n====== BILLING MENU ======")
        print("1. Generate Bill")
        print("2. View Bill")
        print("3. Back to Main Menu")

        choice = input("Enter Choice : ")

        if choice == "1":
            generate_bill()
        elif choice == "2":
            view_bill()
        elif choice == "3":
            break
        else:
            print("Invalid Choice")


def reports_menu():
    while True:
        print("\n====== REPORTS MENU ======")
        print("1. Hospital Summary")
        print("2. Patient Report")
        print("3. Doctor Report")
        print("4. Appointment Report")
        print("5. Billing Report")
        print("6. Back to Main Menu")

        choice = input("Enter Choice : ")

        if choice == "1":
            hospital_summary()
        elif choice == "2":
            patient_report()
        elif choice == "3":
            doctor_report()
        elif choice == "4":
            appointment_report()
        elif choice == "5":
            billing_report()
        elif choice == "6":
            break
        else:
            print("Invalid Choice")

def register_menu():
    while True:
        print("\n====== REGESTERING NEW USER ======")
        print("1. Register New User")
        print("2. Back to Main Menu")

        choice = input("Enter Choice : ")

        if choice == "1":
            register_user()
        elif choice == "2":
            break
        else:
            print("Invalid Choice")


def main():
    setup_database()
    setup_auth()

    if not login():
        return

    while True:
        print("\n========== MEDI-FLOW ==========")
        print("1. Patients")
        print("2. Doctors")
        print("3. Appointments")
        print("4. Billing")
        print("5. View Reports")
        print("6. Register New Hospital Staff")
        print("7. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            patient_menu()
        elif choice == "2":
            doctor_menu()
        elif choice == "3":
            appointment_menu()
        elif choice == "4":
            billing_menu()
        elif choice == "5":
            reports_menu()
        elif choice == "6":
            register_user()
        elif choice == "7":
            print("\nThank You!")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()