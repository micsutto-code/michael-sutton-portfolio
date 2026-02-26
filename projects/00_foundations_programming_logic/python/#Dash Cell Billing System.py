#Dash Cell Billing System

def compute_bill(messages):
        pretax = 5.00

        if messages > 100:
            if messages > 300:
                pretax += (messages - 100) * 0.05
            else:
                pretax += 200 * 0.03
                pretax += (messages - 300) * 0.02

        after_tax = pretax * 1.14
        return round(after_tax, 2)

def process_customers():
        while True:
            area_code = input("Enter area code (or 999 to quit): ")

            if area_code == "999":
                break

            phone_number = input("Enter phone number: ")
            messages = int(input("Enter number of messages: "))

            total_bill = compute_bill(messages)

            print(f"\nCustomer: ({area_code}) {phone_number}")
            print(f"Messages: {messages}")
            print(f"Total Bill: ${total_bill}\n")
    
def filter_over_100():
        while True:
            area_code = input("Enter area code (or 999 to quit): ")

            if area_code == "999":
                break

            phone_number = input("Enter phone number: ")
            messages = int(input("Enter number of messages: "))

            total_bill = compute_bill(messages)

            if messages > 100:
                print(f"\nCustomer: ({area_code}) {phone_number}")
                print(f"Messages: {messages}")
                print(f"Total Bill: ${total_bill}\n")
    
def filter_bill_over_10():
        while True:
            area_code = input("Enter area code (or 999 to quit): ")

            if area_code == "999":
                break

            phone_number = input("Enter phone number: ")
            messages = int(input("Enter number of messages: "))

            total_bill = compute_bill(messages)

            if total_bill > 10:
                print(f"\nCustomer: ({area_code}) {phone_number}")
                print(f"Messages: {messages}")
                print(f"Total Bill: ${total_bill}\n")

def filter_by_area_code():
        target_area_code = input("Enter target area code: ")

        while True:
            area_code = input("Enter area code (or 999 to quit): ")

            if area_code == "999":
                break

            phone_number = input("Enter phone number: ")
            messages = int(input("Enter number of messages: "))

            total_bill = compute_bill(messages)

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