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


