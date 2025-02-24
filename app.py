import os
import streamlit as st
from expense_manager import add_expense, load_expenses, reset_expenses
from visualization import generate_pie_chart, generate_line_chart

def main():
    st.set_page_config(page_title="Finance Tracker", layout="wide")

    # App title and description
    st.title("💰 Finance Tracker and Budget App")
    st.subheader("Track your expenses and stay within budget effortlessly!")

    # Clear existing data for new sessions
    if not os.path.exists("expenses.csv"):
        reset_expenses()  # Ensure clean data for new user

    # Sidebar for input
    st.sidebar.header("Input your data")
    monthly_budget = st.sidebar.number_input("Enter your monthly budget", min_value=0, step=100)
    expense_name = st.sidebar.text_input("Expense Name", placeholder="e.g., Groceries, Rent")
    expense_amount = st.sidebar.number_input("Amount", min_value=0, step=10)
    expense_category = st.sidebar.selectbox("Category", ["Housing", "Food", "Transportation", "Entertainment", "Other"])
    expense_date = st.sidebar.date_input("Date of Expense")
    expense_notes = st.sidebar.text_area("Notes", placeholder="Add any additional details about the expense.")

    if st.sidebar.button("Add Expense", type="primary"):
        add_expense(expense_name, expense_amount, expense_category, expense_date, expense_notes)
        st.sidebar.success("Expense added successfully!")

    # Load and display data
    data = load_expenses()

    if data is not None and not data.empty:
        col1, col2 = st.columns([2, 1])

        with col1:
            st.header("📋 Expenses")
            st.dataframe(data)

        with col2:
            total_expenses = data['Amount'].sum()
            remaining_budget = monthly_budget - total_expenses
            st.metric(label="Total Expenses", value=f"${total_expenses}")
            st.metric(label="Remaining Budget", value=f"${remaining_budget}", delta=-remaining_budget if remaining_budget < 0 else None)

        # Charts
        st.subheader("📊 Expenses by Category")
        st.plotly_chart(generate_pie_chart(data), use_container_width=True)

        st.subheader("📈 Spending Over Time")
        st.plotly_chart(generate_line_chart(data), use_container_width=True)
    else:
        st.info("No expenses recorded yet. Add some to get started!")

if __name__ == "__main__":
    main()
