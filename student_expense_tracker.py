import csv
from datetime import datetime

FILENAME = "expenses.csv"


def load_expenses(filename):
    expenses = []
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses


def save_expenses(filename, expenses):
    with open(filename, "w", newline="") as file:
        fieldnames = ["date", "category", "description", "amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses, amount, category, description, date):
    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    }
    expenses.append(expense)
    return expenses


def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)


def calculate_total_by_category(expenses, category):
    return sum(
        expense["amount"] for expense in expenses if expense["category"] == category
    )


def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print(
            f"{expense['date']} | {expense['category']} | "
            f"{expense['description']} | ₦{expense['amount']:.2f}"
        )


def get_user_menu_choice():
    print("\nStudent Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. View Total by Category")
    print("5. Exit")
    return input("Choose an option: ")


def main():
    expenses = load_expenses(FILENAME)

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            date = datetime.now().strftime("%Y-%m-%d")

            expenses = add_expense(expenses, amount, category, description, date)
            save_expenses(FILENAME, expenses)
            print("Expense added successfully.")

        elif choice == "2":
            display_expenses(expenses)

        elif choice == "3":
            total = calculate_total(expenses)
            print(f"Total expenses: ₦{total:.2f}")

        elif choice == "4":
            category = input("Enter category: ")
            total = calculate_total_by_category(expenses, category)
            print(f"Total for {category}: ₦{total:.2f}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
