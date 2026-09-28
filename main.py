# Enhance it a bit
# Would be good if during booking appointment you can select from the list of doctrs or the list would be visible
# Change the yyyy-mm-dd format in appointments


from modules.database import setup_database
from modules.auth import setup_auth, login
from modules.patients import register_patient, search_patient, update_patient
from modules.doctors import list_doctors
from modules.appointments import book_appointment, view_appointments, cancel_appointment
from modules.billing import generate_bill, view_bill


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
        print("5. Exit")

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
            print("\nThank You!")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()