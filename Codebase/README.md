# 💊 Pharmacy Inventory System

**PS No. 53** | A console-based application in **Python 3** to manage a pharmacy's medicine stock using a **CSV file**.

---

## 📌 Table of Contents
1. [About the Project](#-about-the-project)
2. [Problem Statement](#-problem-statement)
3. [Features](#-features)
4. [Concepts Used](#-concepts-used)
5. [Project Structure](#-project-structure)
6. [Data Format (CSV)](#-data-format-csv)
7. [How to Run](#-how-to-run)
8. [Menu Options](#-menu-options)
9. [How the Program Works](#-how-the-program-works)
10. [Validation Rules](#-validation-rules)
11. [Test Cases](#-test-cases)
12. [Sample Run](#-sample-run)
13. [Limitations and Future Scope](#-limitations-and-future-scope)
14. [Author](#-author)

---

## 📖 About the Project

A medical store has to keep track of many medicines: how many are left, what the price is, and which ones are about to run out. Doing this on paper is slow and error-prone.

This project is a simple **console application** (it runs in the terminal, with no buttons or windows) that does this job. The user can add medicines, view the stock, sell medicines (stock reduces and a bill is generated), delete medicines, and see a low-stock report. All the data is saved in a **CSV file**, so nothing is lost when the program is closed.

---

## 📝 Problem Statement

Develop a console application to manage a pharmacy's medicine stock. The user can:

- add medicines
- view stock
- sell medicines (reducing stock and generating a bill)
- delete medicines
- see a low-stock report

Data is stored in a CSV file.

**Note:** Medicines are stored in `medicines.csv` with columns **ID, Name, Quantity, Price**. IDs start from **M1**. A medicine is **'Low stock'** when its quantity is **below 10**.

---

## ✨ Features

| # | Feature | Description |
|---|---|---|
| 1 | **Add medicine** | Adds a new medicine with an auto-generated ID (M1, M2, M3...) |
| 2 | **View stock** | Shows all medicines with quantity and price |
| 3 | **Sell medicine** | Reduces stock and prints the bill (quantity x price) |
| 4 | **Delete medicine** | Removes a medicine using its ID |
| 5 | **Low stock report** | Lists medicines with quantity below 10 |
| 6 | **Inventory value** | Total value of all stock (sum of quantity x price) |
| 7 | **Exit** | Closes the program |

Extra: data is **saved to the CSV file after every change**, and the program is protected against negative values and over-selling.

---

## 🧠 Concepts Used

- **Python 3** basics: variables, data types (`int`, `float`, `str`)
- **List**: stores all medicines
- **Dictionary**: stores one medicine (`ID`, `Name`, `Quantity`, `Price`)
- **List of dictionaries**: the main data structure of the project
- **CSV module**: `csv.DictReader` and `csv.DictWriter` for reading and writing the file
- **Functions**: each feature is a separate function
- **Loops**: `while True` for the menu, `for` for going through medicines
- **Conditions**: `if / elif / else` for decisions and validation
- **Exception handling**: `try / except FileNotFoundError` when the file does not exist yet
- **CRUD operations**: Create (add), Read (view), Update (sell), Delete

---

## 📁 Project Structure

```
Pharmacy-Inventory-System/
│
├── Codebase/
│   └── Pharmacy_Inventory.py   # Main program (single .py file)
    └── README.md  
├── TestCases/                  # Screenshots of the test cases
└── README.md                   # Project documentation (this file)
```

---

## 🗂️ Data Format (CSV)

Medicines are stored in `medicines.csv`:

```csv
ID,Name,Quantity,Price
M1,Paracetamol,50,2.50
M2,Cetirizine,8,5.00
M3,Amoxicillin,30,12.00
```

| Column | Meaning | Type in Python |
|---|---|---|
| ID | Unique ID, starts from M1 | `str` |
| Name | Medicine name | `str` |
| Quantity | Units in stock | `int` |
| Price | Price per unit | `float` |

In the program, each row is loaded as a dictionary, for example:

```python
{"ID": "M1", "Name": "Paracetamol", "Quantity": 50, "Price": 2.5}
```

and all medicines together form a **list of dictionaries**.

---

## ▶️ How to Run

**Requirements:** Python 3 installed (no extra libraries needed, `csv` is built into Python).

1. Clone the repository and go into the `Codebase` folder (or download it as a ZIP and open the folder in VS Code):
   ```bash
   git clone https://github.com/sampada-code14/Pharmacy-Inventory-System.git
   cd Pharmacy-Inventory-System/Codebase
   ```
2. Run the program from the terminal:
   ```bash
   python Pharmacy_Inventory.py
   ```
   (On some systems use `python3 Pharmacy_Inventory.py`.)
3. Type the number of the option you want and press **Enter**.

> You do not have to create `medicines.csv` yourself. The program creates it automatically when the first medicine is added.

---

## 🧾 Menu Options

```
--- Pharmacy Inventory System ---
1. Add medicine
2. View stock
3. Sell medicine
4. Delete medicine
5. Low stock report
6. Inventory value
7. Exit
Enter choice:
```

| Choice | What you type next |
|---|---|
| `1` | Name, Quantity, Price |
| `2` | Nothing (shows the stock) |
| `3` | Medicine ID, Quantity to sell |
| `4` | Medicine ID |
| `5` | Nothing (shows low-stock medicines) |
| `6` | Nothing (shows total value) |
| `7` | Nothing (exits) |

---

## ⚙️ How the Program Works

**Program flow:**

```
Start
  │
  ▼
Load medicines.csv into a list of dictionaries
  │
  ▼
┌─► Show menu ──► User enters a choice
│                     │
│     ┌───────────────┼───────────────────────┐
│     ▼               ▼                       ▼
│   Add / Sell /    View / Low stock /      Exit (7)
│   Delete          Inventory value            │
│     │               │                       ▼
│     ▼               │                      End
│   Save list to CSV  │
│     │               │
└─────┴───────────────┘
```

**Main functions:**

| Function | Purpose |
|---|---|
| `load_medicines()` | Reads the CSV file and returns a list of dictionaries. Returns an empty list if the file does not exist. |
| `save_medicines(medicines)` | Writes the list back to the CSV file (called after every change). |
| `generate_id(medicines)` | Finds the highest ID number and returns the next one (e.g. M4). This avoids duplicate IDs after a delete. |
| `find_medicine(medicines, med_id)` | Searches for a medicine by ID. Returns it, or `None` if not found. |
| `add_medicine(medicines)` | Takes name, quantity, price; validates; adds the medicine. |
| `view_stock(medicines)` | Prints all medicines. |
| `sell_medicine(medicines)` | Validates, calculates bill, reduces stock, saves. |
| `delete_medicine(medicines)` | Removes a medicine by ID. |
| `low_stock_report(medicines)` | Prints medicines with quantity < 10. |
| `inventory_value(medicines)` | Adds up quantity x price for all medicines. |
| `main()` | Loads data and runs the menu loop. |

**Formulas:**
- Bill = `quantity x price`
- Stock after sale = `old stock - quantity sold`
- Total inventory value = sum of (`quantity x price`) for every medicine

---

## 🛡️ Validation Rules

| Situation | Program response |
|---|---|
| Negative quantity or price while adding | Rejected with an error message |
| Selling quantity of 0 or less | Rejected |
| Selling more than available stock | `Insufficient stock. Available: <n>` (stock does not change) |
| Medicine ID not found (sell / delete) | `Medicine not found.` |
| Invalid menu choice | `Invalid choice. Enter 1 to 7.` |
| `medicines.csv` does not exist yet | Program starts with an empty list (no crash) |

---

## ✅ Test Cases

### Test Case 1: Normal Input

**Input**
```
Menu option 1 (Add)
Name: Paracetamol
Quantity: 50
Price: 2.50
```
**Expected Output**
```
Medicine added. ID: M1 | Paracetamol | Qty: 50 | Price: 2.50
```
**Result:** ✅ Pass

📸 Screenshot: see the `TestCases` folder.

---

### Test Case 2: Boundary / Minimum Input

**Setup:** M1, Paracetamol, Qty 50, Price 2.50
**Input**
```
Menu option 3 (Sell)
ID: M1
Quantity: 50 (entire stock)
```
**Expected Output**
```
Sold 50 units. Bill: 125.00
Stock left: 0 | Out of stock!
```
**Result:** ✅ Pass

📸 Screenshot: see the `TestCases` folder.

---

### Test Case 3: Invalid Input

**Setup:** M1, Paracetamol, Qty 5, Price 2.50
**Input**
```
Menu option 3 (Sell)
ID: M1
Quantity: 8
```
**Expected Output**
```
Insufficient stock. Available: 5
```
**Result:** ✅ Pass

📸 Screenshot: see the `TestCases` folder.

---

### Test Case 4: Different Valid Scenario

**Setup:** `medicines.csv` contains
```
M1,Paracetamol,50,2.50
M2,Cetirizine,8,5.00
M3,Amoxicillin,30,12.00
```
**Input**
```
(a) Menu option 5 (Low stock report)
(b) Menu option 4 (Delete): ID M3
(c) Menu option 6 (Inventory value)
```
**Expected Output**
```
(a) M2 | Cetirizine | Qty: 8 (Low stock)
(b) Medicine M3 deleted.
(c) Total inventory value: 165.00
```
**Calculation for (c):** M1 → 50 x 2.50 = 125.00, M2 → 8 x 5.00 = 40.00, so total = **165.00** (M3 was already deleted).

**Result:** ✅ Pass

📸 Screenshot: see the `TestCases` folder.

---

### Test Summary

| Test Case | Type | Result |
|---|---|---|
| 1 | Normal input | ✅ Pass |
| 2 | Boundary / minimum input | ✅ Pass |
| 3 | Invalid input | ✅ Pass |
| 4 | Different valid scenario | ✅ Pass |

---

## 💻 Sample Run

```
--- Pharmacy Inventory System ---
1. Add medicine
2. View stock
3. Sell medicine
4. Delete medicine
5. Low stock report
6. Inventory value
7. Exit
Enter choice: 1
Name: Paracetamol
Quantity: 50
Price: 2.50
Medicine added. ID: M1 | Paracetamol | Qty: 50 | Price: 2.50

Enter choice: 3
ID: M1
Quantity: 20
Sold 20 units. Bill: 50.00
Stock left: 30

Enter choice: 6
Total inventory value: 75.00

Enter choice: 7
Goodbye!
```

---

## ⚠️ Limitations and Future Scope

**Current limitations**
- If the user types text where a number is expected (for example `abc` as quantity), the program may stop with an error. This can be handled with `try / except ValueError`.
- Two medicines with the same name get different IDs (no duplicate-name check).
- Only one user can use it at a time (no login).

**Future improvements**
- Handle invalid number input with `try / except`
- Search medicine by name
- Update price or restock an existing medicine
- Save a bill history / sales report
- Add expiry date tracking
- Build a GUI (Tkinter) or a web version, or use a database (SQLite)

---

## 👩‍💻 Author

- **Name:** Sampada Kumari Singh
- **Roll No.:** RU-26-00092
- **Course / Year:** B.Tech 1st Year
- **College:** Rungta International Skills University
- **GitHub:** [sampada-code14](https://github.com/sampada-code14)

---

⭐ *Made as part of the First Year Python Project (PS 53).*
