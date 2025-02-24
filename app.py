# app.py
import streamlit as st
from expense_manager import add_expense, load_expenses
from visualization import generate_pie_chart, generate_line_chart
import pandas as pd

def main():
    # Enhanced UI styling
    st.set_page_config(page_title="Finance Tracker", layout="wide")

    st.markdown(
        """<style>
        .main { background-color: #f5f5f5; padding: 20px; }
        .sidebar { background-color: #e8f0fe; padding: 20px; border-radius: 10px; }
        h1 { color: #2d4f6c; }
        h2, h3 { color: #3a607d; }
        </style>""",
        unsafe_allow_html=True,
    )

    st.title("💰 Finance Tracker and Budget App")
    st.subheader("Track your expenses and stay within budget effortlessly!")

    # Welcome images and introduction
    if "logged_in" not in st.session_state:
        st.image("welcome_image.jpg", caption="Welcome to Finance Tracker", use_column_width=True)
        st.markdown("### Manage your budget like a pro! 💼")
        st.markdown("#### Features:")
        st.markdown("- Add and track your expenses\n- Visualize spending with charts\n- Stay on top of your budget")

        st.sidebar.header("Login")
        with st.sidebar.form("login_form"):
            user_name = st.text_input("Name")
            user_phone = st.text_input("Phone Number")
            login_button = st.form_submit_button("Login")

        if login_button and user_name and user_phone:
            st.session_state.logged_in = True
            st.session_state.user_name = user_name
            st.session_state.user_phone = user_phone
            st.success(f"Welcome, {user_name}!")

    if "logged_in" in st.session_state and st.session_state.logged_in:
        # Sidebar for user inputs
        st.sidebar.header("Input your data")

        # Budget input
        monthly_budget = st.sidebar.number_input("Enter your monthly budget", min_value=0, step=100, help="Your total monthly budget in USD.")

        # Expense input
        st.sidebar.subheader("Add your expenses")
        expense_name = st.sidebar.text_input("Expense Name", placeholder="e.g., Groceries, Rent")
        expense_amount = st.sidebar.number_input("Amount", min_value=0, step=10, help="Amount spent in USD.")
        expense_category = st.sidebar.selectbox(
            "Category", ["Housing", "Food", "Transportation", "Entertainment", "Other"], help="Select the category for your expense."
        )

        # Additional details input
        st.sidebar.subheader("Additional Details")
        expense_date = st.sidebar.date_input("Date of Expense", help="Enter the date of this expense.")
        expense_notes = st.sidebar.text_area("Notes", placeholder="Add any additional details about the expense.")

        if st.sidebar.button("Add Expense", type="primary"):
            add_expense(expense_name, expense_amount, expense_category, expense_date, expense_notes)
            st.sidebar.success("Expense added successfully!")

        # Display data and charts
        data = load_expenses()

        if data is not None:
            col1, col2 = st.columns([2, 1])

            with col1:
                st.header("📋 Expenses")
                st.dataframe(data, height=400, width=700)

            with col2:
                total_expenses = data['Amount'].sum()
                remaining_budget = monthly_budget - total_expenses
                st.metric(label="Total Expenses", value=f"${total_expenses}")
                st.metric(label="Remaining Budget", value=f"${remaining_budget}", delta=-remaining_budget if remaining_budget < 0 else None)

            # Pie chart for categories
            st.subheader("📊 Expenses by Category")
            category_chart = generate_pie_chart(data)
            st.plotly_chart(category_chart, use_container_width=True)

            # Line chart for spending trend
            st.subheader("📈 Spending Over Time")
            spending_chart = generate_line_chart(data)
            st.plotly_chart(spending_chart, use_container_width=True)
        else:
            st.info("No expenses recorded yet. Add some to get started!")

if __name__ == "__main__":
    main()
