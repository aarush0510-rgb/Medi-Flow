import json
import os

DATA_DIR = "data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


def load_table(table_name):
    """Load a table (e.g. 'patients') as a dict keyed by ID."""
    path = os.path.join(DATA_DIR, f"{table_name}.json")
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "r") as f:
            return json.load(f)
    return {}


def save_table(table_name, data):
    """Save a table dict back to its JSON file."""
    path = os.path.join(DATA_DIR, f"{table_name}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def setup_database():
    doctors = load_table("doctors")

    defaults = [
        ("D101", "Dr. Sharma", "General Medicine", 500),
        ("D102", "Dr. Patel", "Cardiology", 800),
        ("D103", "Dr. Khan", "Orthopedic", 700),
        ("D104", "Dr. Singh", "Dermatology", 600),
        ("D105", "Dr. Mehta", "Dentist", 400),
        ("D106", "Dr. Verma", "Neurology", 900),
        ("D107", "Dr. Iyer", "Pediatrics", 550),
        ("D108", "Dr. Gupta", "ENT", 500),
        ("D109", "Dr. Reddy", "Ophthalmology", 650),
        ("D110", "Dr. Nair", "Gynecology", 750),
    ]

    for doctor_id, name, department, fee in defaults:
        if doctor_id not in doctors:
            doctors[doctor_id] = {
                "doctor_id": doctor_id,
                "name": name,
                "department": department,
                "fee": fee
            }

    save_table("doctors", doctors)