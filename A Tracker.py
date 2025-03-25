import csv
from datetime import datetime

EXPENSES_FILE = 'expenses.csv'

# Function to add an expense
def add_expense(date, category, description, amount):
    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    try:
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\nDate        | Category     | Description       | Amount")
            print("-" * 50)
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]} | ${row[3]}")
    except FileNotFoundError:
        print("No expenses found.")

# Function to get total expenses
def total_expenses():
    total = 0.0
    try:
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[3])
        print(f"\nTotal Expenses: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses found.")

# Main menu
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            date = datetime.now().strftime('%Y-%m-%d')
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            add_expense(date, category, description, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
