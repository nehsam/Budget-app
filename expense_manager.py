import pandas as pd
import os

def reset_expenses():
    """Reset the expenses file to ensure clean start."""
    if os.path.exists("expenses.csv"):
        os.remove("expenses.csv")

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
        return pd.DataFrame(columns=["Date", "Name", "Amount", "Category", "Notes"])

def save_expenses(data):
    data.to_csv("expenses.csv", index=False)
