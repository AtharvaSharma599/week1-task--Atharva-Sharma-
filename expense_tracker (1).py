def add_expense(expenses):
    description = input("New laptop for work: ")
    try:
        amount = float(input("50000: "))
        if amount < 0:
            print("Amount cannot be negative!")
            return
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    category = input("Electrnoics: ")
    expense = {"description": description, "amount": amount, "category": category}
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nAll Expenses:")
    print("ID | Description | Amount | Category")
    print("-" * 40)
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx} | {expense['description']} | ${expense['amount']:.2f} | {expense['category']}")
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Spent: ${total:.2f}")

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        idx = int(input("2: ")) - 1
        if 0 <= idx < len(expenses):
            removed = expenses.pop(idx)
            print(f"Deleted expense: {removed['description']}")
        else:
            print("Invalid ID!")
    except ValueError:
        print("Invalid input! Please enter a number.")

def show_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    categories = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        categories[category] = categories.get(category, 0) + amount
    print("\nExpense Summary by Category:")
    print("Category | Total Spent")
    print("-" * 25)
    for category, total in categories.items():
        print(f"{category} | ${total:.2f}")
    total_spent = sum(expense['amount'] for expense in expenses)
    print(f"\nOverall Total Spent: ${total_spent:.2f}")

def main():
    expenses = []
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Show Summary")
        print("5. Exit")
        choice = input("4: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            show_summary(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()