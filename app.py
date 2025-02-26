import streamlit as st
from auth import login_user, logout_user, is_logged_in
from data_handler import save_expense, get_all_expenses
from visualization import generate_charts
from ui_components import render_app_details, render_table

# Streamlit page configuration
st.set_page_config(page_title="Budget Planner", page_icon=":moneybag:", layout="wide")

# Applying the theme with hardcoded colors
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f9;
            color: #333333;
        }
        .stButton>button {
            background-color: #6c63ff;
            color: white;
            border-radius: 5px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

if is_logged_in():
    user = st.session_state['user']
    st.sidebar.success(f"Welcome, {user['name']}!")
    if st.sidebar.button("Logout"):
        logout_user()
        st.experimental_rerun()

    st.sidebar.image("Budget.jpg", use_container_width=True)

    # Welcome message for logged-in users
    st.title(f"Welcome, {user['name']}!")
    render_app_details()

    # Sidebar inputs for income and expenses
    st.sidebar.header("Add Your Expenses")
    income = st.sidebar.number_input("Enter your Income:", min_value=0.0, format="%.2f")
    expense_name = st.sidebar.selectbox("Expense Name:", ["Food", "Travel", "Shopping", "Bills", "Others"])
    expense_amount = st.sidebar.number_input("Expense Amount:", min_value=0.0, format="%.2f")
    expense_details = st.sidebar.text_area("Expense Details:")

    if st.sidebar.button("Add Expense"):
        save_expense(user, income, expense_name, expense_amount, expense_details)
        st.sidebar.success("Expense added successfully!")

    # Display expense table
    expenses = get_all_expenses(user)
    st.subheader("Expense Table")
    render_table(expenses)

    # Generate and display charts
    st.subheader("Expense Analysis")
    generate_charts(expenses, income)
else:
    st.title("Welcome to NEHA's Budget Planner")
    st.write("Manage your expenses and analyze your spending habits effectively.")
    login_user()
