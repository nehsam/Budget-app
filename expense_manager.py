import pandas as pd
import os

USER_LOG_FILE = "users.csv"

def register_user(name, phone_number):
    if not os.path.exists(USER_LOG_FILE):
        users = pd.DataFrame(columns=["Name", "Phone Number"])
    else:
        users = pd.read_csv(USER_LOG_FILE)

    if phone_number not in users["Phone Number"].values:
        new_user = pd.DataFrame({"Name": [name], "Phone Number": [phone_number]})
        users = pd.concat([users, new_user], ignore_index=True)
        users.to_csv(USER_LOG_FILE, index=False)

def get_users():
    try:
        return pd.read_csv(USER_LOG_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Phone Number"])

def add_expense(name, amount, category, date, notes, user_file):
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
        data = load_expenses(user_file)

        if data is not None:
            data = pd.concat([data, new_entry], ignore_index=True)
        else:
            data = new_entry

        save_expenses(data, user_file)

def load_expenses(user_file):
    try:
        return pd.read_csv(user_file)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Name", "Amount", "Category", "Notes"])

def save_expenses(data, user_file):
    data.to_csv(user_file, index=False)
