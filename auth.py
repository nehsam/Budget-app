import streamlit as st
from data_handler import load_user_data

def login_user():
    st.sidebar.title("Login")
    st.image("Budget.jpg", use_container_width=True)  # Adding image to the login form
    username = st.sidebar.text_input("Enter your Name:")
    phone_number = st.sidebar.text_input("Enter your Phone Number:")

    if st.sidebar.button("Login"):
        if username and phone_number.isnumeric():
            user_data = load_user_data()
            if phone_number in user_data:
                st.sidebar.success(f"Welcome back, {user_data[phone_number]['name']}!")
                st.session_state["user"] = {"name": user_data[phone_number]["name"], "phone": phone_number}
            else:
                st.sidebar.success(f"Welcome, {username}!")
                st.session_state["user"] = {"name": username, "phone": phone_number}
            return st.session_state["user"]
        else:
            st.sidebar.error("Please provide valid information.")
    return None

def logout_user():
    if "user" in st.session_state:
        del st.session_state["user"]

def is_logged_in():
    return "user" in st.session_state
