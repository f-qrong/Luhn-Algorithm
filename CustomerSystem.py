# Qianrong & Yafei
import csv

def printMenu():
    menu = [
        "1. Enter Customer Information",
        "2. Generate Customer data file",
        "3. Quit",
    ]
    print("\nCustomer and Sales System\n")

    for i in menu:
        print(i)

    print("\nEnter menu option(1-3)\n")


def validatePostalCode(postal_code):
    valid_postal_code = set()

    try:

        with open("postal_codes.csv", "r", encoding="utf-8", errors="ignore") as file:
            lines = file.readlines()

        for line in lines[1:]:
            columns = line.strip().split('|')
            postal_code_in_file = columns[0]
            if len(postal_code_in_file) == 3:
                valid_postal_code.add(postal_code_in_file)

    except FileNotFoundError:
        print("Error: postal_codes.csv file not found.")
        return False

    if len(postal_code) < 3:
        print("Error: Postal code must be at least 3 characters long.")
        return False
    if postal_code[:3] not in valid_postal_code:
        print(f"Error: Invalid postal code prefix {postal_code[:3]}.")
        return False

    return True


def validateCreditCard(credit_card_number):
    credit_card_number = credit_card_number.strip()
    if len(credit_card_number) < 9:
        print("Invalid credit card number: must1 be at least 9 digits.")
        return False

    for number in credit_card_number:
        if number < "0" or number > "9":
            print("Invalid credit card number: must contain only digits.")
            return False

    def luhn_check(card_number):
        reversed_digit = []
        for i in range(len(card_number) - 1, -1, -1):
            reversed_digit.append(int(card_number[i]))

        sum1 = 0
        sum2 = 0

        for i in range(len(reversed_digit)):
            digit = reversed_digit[i]
            if i % 2 == 0:
                sum1 += digit
            else:
                doubled = digit * 2
                if doubled > 9:
                    sum2 += (doubled - 9)
                else:
                    sum2 += doubled
        return (sum1 + sum2) % 10

    if luhn_check(credit_card_number) == 0:
        return True
    else:
        print("Invalid credit card number")
        return False


def enterCustomerInfo(customers, customer_id):
    first_name = input("Please enter your first name: ").strip()
    last_name = input("Please enter your last name: ").strip()
    city = input("Please enter the city you live in: ").strip()

    while True:
        postal_code = input("Please enter the postal code: ").strip()
        if validatePostalCode(postal_code):
            break

    while True:
        credit_card_number = input("Please enter your Credit Card Number: ").strip()
        if validateCreditCard(credit_card_number):
            break

    customer_data = {
        "ID": customer_id,
        "First Name": first_name,
        "Last Name": last_name,
        "City": city,
        "Postal Code": postal_code,
        "Credit Card Number": credit_card_number
    }
    customers.append(customer_data)
    print(f"Customer #{customer_id} added successfully!")
    return customer_id + 1, customers


def generateCustomerDataFile(customers):
    if not customers:
        print("No customer data available.")
    else:
        filename = input("Enter the output file name (e.g., customers.csv): ").strip()
        if not filename.endswith(".csv"):
            filename += ".csv"

        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=customers[0].keys())
                writer.writeheader()
                writer.writerows(customers)
            print(f"Customer data successfully saved to '{filename}'.")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")


userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "3"

customers = []
customer_id = 1

while userInput != exitCondition:
    printMenu()
    userInput = input().strip()

    if userInput == enterCustomerOption:
        customer_id, customers = enterCustomerInfo(customers, customer_id)

    elif userInput == generateCustomerOption:
        generateCustomerDataFile(customers)

    elif userInput == exitCondition:
        print("Program Terminated")
        break
    else:
        print("Please type in a valid option (A number from 1-3)")
