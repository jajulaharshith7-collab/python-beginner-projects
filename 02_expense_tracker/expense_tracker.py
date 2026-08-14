expenses = []

def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def show_expenses():
    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print("Category:", expense["category"])
        print("Amount:", expense["amount"])
        print()

def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expense:", total)

while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")