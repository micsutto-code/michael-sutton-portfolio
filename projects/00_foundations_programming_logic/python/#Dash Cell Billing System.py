import csv
from datetime import datetime

#Dash Cell Billing System

def compute_bill(messages):
        pretax = 5.00

        if messages > 100:
            if messages <= 300:
                pretax += (messages - 100) * 0.03
            else:
                pretax += 200 * 0.03
                pretax += (messages - 300) * 0.02

        after_tax = pretax * 1.14
        return round(after_tax, 2)

def prompt_area_code(prompt="Enter area code (or 999 to quit): "):
    while True:
        area = input(prompt).strip()
        if area == "999":
            return area
        if area.isdigit() and len(area) == 3:
            return area
        print("Invalid area code. Enter 3 digits (e.g., 317) or 999 to quit.")


def prompt_phone_number(prompt="Enter phone number (7 digits): "):
    while True:
        phone = input(prompt).strip().replace("-", "")
        if phone.isdigit() and len(phone) == 7:
            return phone
        print("Invalid phone number. Enter 7 digits (e.g., 5551234).")


def prompt_int(prompt, min_value=0):
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            val = None
        if val is not None and val >= min_value:
            return val
        print(f"Invalid input. Enter a whole number >= {min_value}.")

def log_record(area_code, phone_number, messages, total_bill, path="billing_records.csv"):
    row = {
        "timestamp": datetime.utcnow().isoformat(),
        "area_code": area_code,
        "phone_number": phone_number,
        "messages": messages,
        "total_bill": total_bill,
    }

    write_header = False
    try:
        with open(path, "r", newline="") as _:
            pass
    except FileNotFoundError:
        write_header = True

    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if write_header:
            writer.writeheader()
        writer.writerow(row)

def process_customers():
        while True:
            area_code = prompt_area_code()

            if area_code == "999":
                break

            phone_number = prompt_phone_number()
            messages = prompt_int("Enter number of messages: ", min_value=0)

            total_bill = compute_bill(messages)
            log_record(area_code, phone_number, messages, total_bill)

            print(f"\nCustomer: ({area_code}) {phone_number}")
            print(f"Messages: {messages}")
            print(f"Total Bill: ${total_bill}\n")
    
def filter_over_100():
        while True:
            area_code = prompt_area_code()
            if area_code == "999":
                break

            phone_number = prompt_phone_number()
            messages = prompt_int("Enter number of messages: ", min_value=0)

            total_bill = compute_bill(messages)
            log_record(area_code, phone_number, messages, total_bill)

            if messages > 100:
                print(f"\nCustomer: ({area_code}) {phone_number}")
                print(f"Messages: {messages}")
                print(f"Total Bill: ${total_bill}\n")
    
def filter_bill_over_10():
        while True:
            area_code = prompt_area_code()

            if area_code == "999":
                break

            phone_number = prompt_phone_number()
            messages = prompt_int("Enter number of messages: ", min_value=0)

            total_bill = compute_bill(messages)
            log_record(area_code, phone_number, messages, total_bill)

            if total_bill > 10:
                print(f"\nCustomer: ({area_code}) {phone_number}")
                print(f"Messages: {messages}")
                print(f"Total Bill: ${total_bill}\n")

def filter_by_area_code():
        target_area_code = input("Enter target area code: ")

        while True:
            area_code = prompt_area_code()

            if area_code == "999":
                break

            phone_number = prompt_phone_number()
            messages = prompt_int("Enter number of messages: ", min_value=0)

            total_bill = compute_bill(messages)
            log_record(area_code, phone_number, messages, total_bill)

            if area_code == target_area_code:
                print(f"\nCustomer: ({area_code}) {phone_number}")
                print(f"Messages: {messages}")
                print(f"Total Bill: ${total_bill}\n")

def main():
        print("Dash Cell Billing System!")
        print("1. Process Customers")
        print("2. Filter Customers with >100 Messages")
        print("3. Filter Customers with Bill > $10")
        print("4. Filter Customers by Area Code")
        print("5. Exit")
 
        choice = input("Select an option:  ")

        if choice == "1":
            process_customers()
        elif choice == "2":
            filter_over_100()
        elif choice == "3":
            filter_bill_over_10()
        elif choice == "4":
            filter_by_area_code()
        elif choice == "5":
            print("Goodbye!")
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
        main()  