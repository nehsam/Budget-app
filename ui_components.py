# ui_components.py
import streamlit as st

def render_app_details():
    st.write("Easily track your expenses and make informed decisions.")

def render_table(expenses):
    if not expenses.empty:
        st.dataframe(expenses)
    else:
        st.info("No expenses recorded yet.")
