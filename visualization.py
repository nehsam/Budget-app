# visualization.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def generate_charts(expenses, total_income):
    if expenses.empty:
        st.info("No expenses to display yet.")
        return

    # Expense pie chart
    fig, ax = plt.subplots()
    grouped_expenses = expenses.groupby("Expense Name")["Expense Amount"].sum()
    remaining_income = total_income - grouped_expenses.sum()
    grouped_expenses["Remaining Income"] = remaining_income

    grouped_expenses.plot.pie(ax=ax, autopct='%1.1f%%', startangle=90)
    ax.set_ylabel("")
    st.pyplot(fig)

    # Income vs Expenses
    fig, ax = plt.subplots()
    total_expenses = expenses["Expense Amount"].sum()
    ax.bar(["Income", "Expenses"], [total_income, total_expenses], color=["green", "red"])
    st.pyplot(fig)
