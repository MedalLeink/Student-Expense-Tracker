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

