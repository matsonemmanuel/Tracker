import sqlite3
from datetime import datetime

#create or connect to the expense tracker database
conn = sqlite3.connect('myexpense_tracker.db')
c = conn.cursor()

#Create the expenses table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
          amount REAL,
          category TEXT,
          description TEXT,
          date DATE 
    )
''')

conn.commit()

def add_expense(amount, category, description):
    #Get the current date
    date = datetime.now().strftime('%Y-%m-%d')

    #Insert the expense into the database
    c.execute('INSERT INTO expenses(amount, category, description, date) VALUES (?, ?, ?, ?)',
              (amount, category, description, date))
    conn.commit()
    print("Expense added successfully!")

def view_expenses():
    #Fetch all the expenses from the database
    c.execute('SELECT * FROM expenses ORDER BY date')
    expenses = c.fetchall()

    #Display the expenses
    if expenses:
        print("ID  | Amount  | Category  | Description                 | Date")
        print("---------------------------------------------------------")
        for expense in expenses:
            print(
                f"{expense[0]:<3} | ${expense[1]:<7.2f} | {expense[2]:<15} | {expense[3]:<27} | {expense[4]}"
            )
    else:
        print("No expense found")

def main():
    while True:
        print("\nExpense Tracker Application")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            amount = float(input("Enter the amount spent: $"))
            category = input("Enter the category: ")
            description = input("Enter a brief description: ")
            add_expense(amount, category, description)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            print("Exiting the Expense Tracker Application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#Close the database connection when the application exists
conn.close()
from datetime import datetime

#create or connect to the expense tracker database
conn = sqlite3.connect('myexpense_tracker.db')
c = conn.cursor()

#Create the expenses table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
          amount REAL,
          category TEXT,
          description TEXT,
          date DATE 
    )
''')

conn.commit()

def add_expense(amount, category, description):
    #Get the current date
    date = datetime.now().strftime('%Y-%m-%d')

    #Insert the expense into the database
    c.execute('INSERT INTO expenses(amount, category, description, date) VALUES (?, ?, ?, ?)',
              (amount, category, description, date))
    conn.commit()
    print("Expense added successfully!")

def view_expenses():
    #Fetch all the expenses from the database
    c.execute('SELECT * FROM expenses ORDER BY date')
    expenses = c.fetchall()

    #Display the expenses
    if expenses:
        print("ID  | Amount  | Category  | Description                 | Date")
        print("---------------------------------------------------------")
        for expense in expenses:
            print(
                f"{expense[0]:<3} | ${expense[1]:<7.2f} | {expense[2]:<15} | {expense[3]:<27} | {expense[4]}"
            )
    else:
        print("No expense found")

def main():
    while True:
        print("\nExpense Tracker Application")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ") 

        if choice == '1':
            amount = float(input("Enter the amount spent: $"))
            category = input("Enter the category: ")
            description = input("Enter a brief description: ")
            add_expense(amount, category, description)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            print("Exiting the Expense Tracker Application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#Close the database connection when the application exists
conn.close()
2
        