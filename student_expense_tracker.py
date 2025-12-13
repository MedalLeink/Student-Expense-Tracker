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


