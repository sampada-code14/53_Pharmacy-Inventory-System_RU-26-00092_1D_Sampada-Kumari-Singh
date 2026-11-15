# PS 53 - Pharmacy Inventory System
# Language: Python 3
# Concepts: Dictionaries, Lists, CSV, CRUD

import csv

FILE_NAME = "medicines.csv"
COLUMNS = ["ID", "Name", "Quantity", "Price"]

# ---------- STEP 1: To Bring Data From File and Then Write Data In File ---------

def load_medicines():                                # Empty list
    medicines = []
    try:
        file = open(FILE_NAME, "r")
        reader = csv.DictReader(file, fieldnames=COLUMNS)
        for row in reader:
            if row["ID"] == "ID":                     # Skip header line
                continue
            medicine = {
                "ID": row["ID"],
                "Name": row["Name"],
                "Quantity": int(row["Quantity"]),
                "Price": float(row["Price"])
            }
            medicines.append(medicine)
        file.close()
    except FileNotFoundError:                           # If the file isn't made yet
        pass
    return medicines

def save_medicines(medicines):
    file = open(FILE_NAME, "w", newline="")
    writer = csv.DictWriter(file, fieldnames=COLUMNS)
    writer.writeheader()
    for medicine in medicines:
        writer.writerow(medicine)
    file.close()

# ---------- STEP 2: Small Helper Functions ----------

def generate_id(medicines):
    biggest = 0
    for medicine in medicines:
        number = int(medicine["ID"][1:])                # "M12" -> "12" -> 12
        if number > biggest:
            biggest = number
    return "M" + str(biggest + 1)

def find_medicine(medicines, med_id):
    for medicine in medicines:
        if medicine["ID"] == med_id:
            return medicine
    return None                                     # Not Found


# ---------- STEP 3: CRUD Functions ----------

def add_medicine(medicines):
    name = input("Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    if quantity < 0 or price < 0:
        print("Quantity and price cannot be negative.")
        return

    medicine = {
        "ID": generate_id(medicines),
        "Name": name,
        "Quantity": quantity,
        "Price": price
    }
    medicines.append(medicine)
    save_medicines(medicines)
    print("Medicine added. ID:", medicine["ID"], "|", name,
          "| Qty:", quantity, "| Price: " + format(price, ".2f"))

def view_stock(medicines):
    if len(medicines) == 0:
        print("No medicines in stock.")
        return
    for medicine in medicines:
        print(medicine["ID"], "|", medicine["Name"], "| Qty:",
            medicine["Quantity"], "| Price:", format(medicine["Price"], ".2f"))

def sell_medicine(medicines):
    med_id = input("ID: ")
    medicine = find_medicine(medicines, med_id)

    if medicine is None:
        print("Medicine not found.")
        return

    quantity = int(input("Quantity: "))

    if quantity <= 0:
        print("Quantity must be more than 0.")
        return

    if quantity > medicine["Quantity"]:
        print("Insufficient stock. Available:", medicine["Quantity"])
        return

    bill = quantity * medicine["Price"]
    medicine["Quantity"] = medicine["Quantity"] -  quantity
    save_medicines(medicines)

    print("Sold", quantity, "units.Bill:", format(bill, ".2f"))
    if medicine["Quantity"] == 0:
        print("Stock left: 0 | Out of stock!")
    else:
        print("Stock left:", medicine["Quantity"])

def delete_medicine(medicines):
    med_id = input("ID: ")
    medicine = find_medicine(medicines, med_id)

    if medicine is None:
        print("Medicine not found.")
        return

    medicines.remove(medicine)
    save_medicines(medicines)
    print("Medicines", med_id, "deleted.")

def low_stock_report(medicines):
    found = False
    for medicine in medicines:
        if medicine["Quantity"] < 10:
            print(medicine["ID"], "|", medicine["Name"], "| Qty:",
                 medicine["Quantity"], "(Low stock)")
            found = True
    if not found:
            print("No low stock medicines.")

def inventory_value(medicines):
    total = 0
    for medicine in medicines:
        total = total + medicine["Quantity"] * medicine["Price"]
    print("Total inventory value:", format(total, ".2f"))

# ---------- STEP 4: Main Menu ----------

def main():
    medicines = load_medicines()

    while True:
        print("\n--- Pharmacy Inventory System ---")
        print("1. Add medicine")
        print("2. View stock")
        print("3. Sell medicine")
        print("4. Delete medicine")
        print("5. Low stock report")
        print("6. Inventory value")
        print("7. Exit") 
        choice = input("Enter choice: ")

        if choice == "1":
            add_medicine(medicines)
        elif choice == "2":
            view_stock(medicines)
        elif choice == "3":
            sell_medicine(medicines)
        elif choice == "4":
            delete_medicine(medicines)
        elif choice == "5":
            low_stock_report(medicines)
        elif choice == "6":
            inventory_value(medicines)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 to 7.")


main()

    


