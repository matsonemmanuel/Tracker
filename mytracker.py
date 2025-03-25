import tkinter as tk
from tkinter import ttk, messagebox

# Function to add expense
def add_expense():
    name = name_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()

    if not name or not amount or not category:
        messagebox.showwarning("Input Error", "All fields must be filled!")
        return
    
    try:
        amount = float(amount)  # Convert amount to float
    except ValueError:
        messagebox.showwarning("Input Error", "Amount must be a number!")
        return

    expense_list.insert("", "end", values=(name, f"${amount:.2f}", category))
    update_total()
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

# Function to update total expense
def update_total():
    total = 0.0
    for item in expense_list.get_children():
        total += float(expense_list.item(item, "values")[1][1:])  # Extract numeric value
    total_label.config(text=f"Total: ${total:.2f}")

# Function to clear all expenses
def clear_all():
    expense_list.delete(*expense_list.get_children())
    update_total()

# Create main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x450")
root.configure(bg="#f4f4f4")

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

# Frame for input fields
frame = tk.Frame(root, bg="darkgreen", padx=20, pady=20, relief=tk.RIDGE, bd=2)
frame.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Input fields
tk.Label(frame, text="Expense Name:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Amount:", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
amount_entry = tk.Entry(frame, font=("Arial", 12))
amount_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Category:", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
category_entry = tk.Entry(frame, font=("Arial", 12))
category_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="darkgreen")
button_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

ttk.Button(button_frame, text="Add Expense", command=add_expense).grid(row=0, column=0, padx=10, pady=10)
ttk.Button(button_frame, text="Clear All", command=clear_all).grid(row=0, column=1, padx=10, pady=10)

# Expense List
list_frame = tk.Frame(root, bg="darkgreen", padx=10, pady=10, relief=tk.RIDGE, bd=2)
list_frame.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

columns = ("Name", "Amount", "Category")
expense_list = ttk.Treeview(list_frame, columns=columns, show="headings")
expense_list.heading("Name", text="Name")
expense_list.heading("Amount", text="Amount")
expense_list.heading("Category", text="Category")
expense_list.pack()

# Total Label
total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 14, "bold"), bg="Orange")
total_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

# Run the application
root.mainloop()