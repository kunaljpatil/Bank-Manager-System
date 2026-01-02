
# **Bank Manager System (Python Project)**

A simple, menu-driven **Bank Management System** implemented in Python.
This project demonstrates the use of:

* Object-Oriented Programming (OOP)
* Classes & Inheritance
* Data Storage using Dictionaries
* Modular Coding (account.py, man.py, datastore.py, main.py)
* Transaction Reporting

## **📌 Project Structure**

```
bank_manager_system/
│
├── account.py      → Account, Saving, Current classes
├── manager.py          → Manager class (all banking operations)
├── datastore.py    → Datastore (acts as in-memory database)
├── main.py         → Login system + Program entry point
└── README.md       → Documentation
```

---

## **📝 Features**

### **1. Account Management**

* Create Saving Account
* Create Current Account
* Auto-generated Account Number
* Minimum balance rules for saving accounts

### **2. Banking Operations**

* Check Balance
* Deposit Money
* Withdraw Money
* Validation for inactive accounts
* Minimum balance check (₹1000)

### **3. Reporting**

* Every transaction stored in the report log
* End-Day Report shows list of all operations

### **4. Login System**

Simple login with:

```
User ID: admin
Password: 1234
```

---

## **🚀 How to Run the Project**

### **Step 1: Install Python 3**

Make sure Python 3+ is installed.

### **Step 2: Clone the repository**

```
git clone https://github.com/<your-username>/<repo-name>.git
```

### **Step 3: Navigate into the project folder**

```
cd bank_manager_system
```

### **Step 4: Run the main file**

```
python main.py
```

---

## **💡 Technologies Used**

* Python 3
* Object-Oriented Programming (OOP)
* Dictionary-based datastore

---

## **📂 Files Explained**

### **account.py**

Contains:

* `Account` (base class)
* `Saving` (inherits Account)
* `Current` (inherits Account)

### **datastore.py**

Acts like a mini database:

* Stores accounts
* Stores reports

### **man.py**

Handles:

* Account creation
* Deposit
* Withdraw
* Balance check
* End-Day report

### **main.py**

* Login screen
* Calls Manager menu

---

## **📌 Example Flow**

1. Run program
2. Login as admin
3. Create new account
4. Deposit or withdraw money
5. Check balance
6. Print end-day report

---

## **📜 License**

This project is open-source.
You can modify and use it for learning or academic purposes.

---
