# expense_manager.py
import pandas as pd

def add_expense(name, amount, category, date, notes):
    if name and amount > 0:
        new_entry = pd.DataFrame(
            {
                "Date": [date],
                "Name": [name],
                "Amount": [amount],
                "Category": [category],
                "Notes": [notes],
            }
        )
        data = load_expenses()

        if data is not None:
            data = pd.concat([data, new_entry], ignore_index=True)
        else:
            data = new_entry

        save_expenses(data)

def load_expenses():
    try:
        return pd.read_csv("expenses.csv")
    except FileNotFoundError:
        return None

def save_expenses(data):
    data.to_csv("expenses.csv", index=False)
