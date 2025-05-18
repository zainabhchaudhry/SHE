import streamlit as st

def authenticate_user(username, password):
    # Dummy authentication logic
    valid_users = {"user1": "password1", "user2": "password2"}
    return valid_users.get(username) == password

def auth_page():
    st.title("User Authentication")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login Successful!")
            st.session_state["page"] = "Map"  # Redirect to Map page after login
            st.experimental_rerun()  # Refresh the page to apply redirect
        else:
            st.error("Invalid username or password")
