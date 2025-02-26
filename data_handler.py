import pandas as pd
import json
import os

DATA_FILE = "user_data.json"

# Load data from file
def load_user_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Save data to file
def save_user_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Initialize user data
user_data = load_user_data()

def save_expense(user, income, name, amount, details):
    phone = user["phone"]
    if phone not in user_data:
        user_data[phone] = {"name": user["name"], "expenses": []}

    user_data[phone]["expenses"].append({
        "Income": income,
        "Expense Name": name,
        "Expense Amount": amount,
        "Details": details
    })
    save_user_data(user_data)

def get_all_expenses(user):
    phone = user["phone"]
    if phone in user_data and "expenses" in user_data[phone]:
        return pd.DataFrame(user_data[phone]["expenses"])
    return pd.DataFrame()
