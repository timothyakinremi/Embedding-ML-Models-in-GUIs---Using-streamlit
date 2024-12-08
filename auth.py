import streamlit as st
from home import home_page 


def authenticate():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        login_form()
    else: 
        show_authenticated_content()


def login_form():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.authenticated = True
        else:
            st.error("Invalid credentials")


def show_authenticated_content():
    home_page() 
