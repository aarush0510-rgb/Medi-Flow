# 🏥 MediFlow – Hospital Management System

## 1. Project Overview

**MediFlow** is a Python-based Hospital Management System designed to handle some of the basic operations of a hospital through a **Command-Line Interface (CLI)**.

The project allows users to manage doctors and patients, book appointments, handle user login and registration, and generate basic hospital reports.

MediFlow uses **JSON files for local data storage** instead of a traditional database such as SQLite.

This project was developed as an individual college project to apply Python programming concepts in a practical application.

---

## 2. Features

### 👨‍⚕️ Doctor Management

- Add new doctors
- Automatically generate unique Doctor IDs
- View the list of doctors
- Store doctor name, department, and consultation fee

### 🧑 Patient Management

- Register new patients
- Automatically generate unique Patient IDs
- View patient information
- Store patient records locally

### 📅 Appointment Management

- Book appointments for registered patients
- Select doctors using Doctor IDs
- Automatically generate Appointment IDs
- Generate appointment token numbers
- Store appointment date and time
- Validate patient and doctor records before booking

### 🔐 User Authentication

- User registration
- Login system
- Password input through the terminal
- Default administrator account

### 📊 Reports

- Generate hospital-related reports
- View patient, doctor, and appointment information
- Display useful summaries from the stored data

### 💾 Data Storage

- Uses JSON files for data storage
- Data is stored locally on the user's computer
- Separate JSON files are used for different types of records
- Data files are excluded from GitHub using `.gitignore`

---

## 3. Technologies / Tools Used

| Technology / Tool | Purpose                                        |
| ----------------- | ---------------------------------------------- |
| **Python 3**      | Main programming language                      |
| **JSON**          | Local data storage                             |
| **Tabulate**      | Displaying data in formatted tables            |
| **Datetime**      | Handling and validating dates and times        |
| **Getpass**       | Taking password input securely in the terminal |
| **Git & GitHub**  | Version control and project hosting            |
| **VS Code**       | Development environment                        |

---

## 4. Project Structure

```
Medi-Flow
│
├── data
│   ├── appointments.json
│   ├── doctors.json
│   ├── patients.json
│   └── users.json
│
├── modules
│   ├── __init__.py
│   ├── appointments.py
│   ├── auth.py
│   ├── billing.py
│   ├── database.py
│   ├── doctors.py
│   ├── patients.py
│   └── reports.py
│
├── Test
│   └── test.py
│
├── main.py
├── .gitignore
├── README.md
└── statement.md
```

The JSON data files are stored locally and are not included in the GitHub repository because they are added to `.gitignore`.

The JSON data files are stored locally and are not included in the GitHub repository because they are added to `.gitignore`.

---

## 5. Installation & Running the Project

### Step 1 – Install Python

Make sure Python is installed on your computer.

Check the installed version using:

```bash
python --version
```

Python 3.8 or higher is recommended.

### Step 2 – Clone the Repository

Clone the MediFlow repository using:

```bash
git clone <your-github-repository-link>
```

### Step 3 – Open the Project Folder

```bash
cd MediFlow
```

### Step 4 – Install Required Package

MediFlow uses the `tabulate` package.

Install it using:

```bash
pip install tabulate
```

### Step 5 – Run the Project

Run the main program using:

```bash
python main.py
```

The MediFlow menu will then appear in the terminal.

---

## 6. Testing Instructions

MediFlow includes a `test.py` file to test some of the important functions of the project.

Run the test file using:

```bash
python test.py
```

The test program checks:

- JSON data loading
- Doctor ID generation
- Patient ID generation
- Appointment ID generation
- Appointment token generation

A successful test will display messages such as:

```text
✓ Patients data loaded successfully
✓ Doctors data loaded successfully
✓ Appointments data loaded successfully
✓ Users data loaded successfully

✓ Doctor ID generation is working
✓ Patient ID generation is working
✓ Appointment ID generation is working
✓ Token generation is working
```


---

## 7. Data Storage

MediFlow stores its application data locally using JSON files.

The main data files are:

| File                | Purpose                           |
| ------------------- | --------------------------------- |
| `patients.json`     | Stores patient information        |
| `doctors.json`      | Stores doctor information         |
| `appointments.json` | Stores appointment information    |
| `users.json`        | Stores user and login information |

These files are intentionally excluded from GitHub using `.gitignore`.


---

## 8. Screenshots

See the screenshots folder for sample runs of the program:

Screenshots include:

1. **Main Menu**
2. **Doctor Management**
3. **Patient Registration**
4. **Appointment Booking**
5. **Reports**
6. **Testing Output**


## 9. Project Purpose

MediFlow was developed as an individual college project to apply Python programming concepts in a practical system.

The project helped demonstrate the use of:

- Functions
- Modules
- Lists and dictionaries
- File handling
- JSON
- Exception handling
- Authentication
- Data management
- Basic software testing

---

## 10. Author

***Aarush Bishnoi***

MediFlow was developed as an individual Python project for academic and learning purposes.

---

## 11. Disclaimer

MediFlow is an educational project and is **not intended for use as an actual hospital management system**.

Real patient information, passwords, or other sensitive information should not be stored in the project.
