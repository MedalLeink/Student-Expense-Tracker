from student_expense_tracker import (
    add_expense,
    calculate_total,
    calculate_total_by_category
)



def test_calculate_total():
    expenses = [
        {"amount": 100},
        {"amount": 50},
        {"amount": 25},
    ]
    result = calculate_total(expenses)
    assert result == 175

    expenses.append({"amount": 25})
    assert calculate_total(expenses) == 200


def test_calculate_total_by_category():
    expenses = [
        {"amount": 50, "category": "Food"},
        {"amount": 30, "category": "Transport"},
        {"amount": 20, "category": "Food"},
    ]

    assert calculate_total_by_category(expenses, "Food") == 70
    assert calculate_total_by_category(expenses, "Transport") == 30


def test_add_expense():
    expenses = []
    add_expense(expenses, 40, "Snacks", "Chips", "2025-12-08")

    
