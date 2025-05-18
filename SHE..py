import os
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from utils.auth import authenticate_user
from utils.payments import process_payment

def load_lottieurl(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to load animation from URL.")
            return None
    except Exception as e:
        st.error(f"Error loading animation from URL: {e}")
        return None

def landing_page():
    welcome_animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_touohxv0.json")
    st.markdown("### Welcome to SHE")
    if welcome_animation:
        st_lottie(welcome_animation, height=250, width=250, key="welcome")
    st.write(
        "Join us in revolutionizing the ride-hailing experience for women. SHE is designed "
        "to provide a safe, secure, and comfortable ride-hailing service."
    )
    if st.button("Get Started"):
        st.session_state["page"] = "Auth"

def home_page():
    st.title('Welcome to SHE - Women-Only Ride-Hailing App')
    st.markdown("### Safe. Secure. SHE.")
    st.write("Your ultimate safe ride-hailing solution designed exclusively for women. Driven by women, for women.")
    st.markdown("---")
    st.write("Experience security and comfort while commuting. Join SHE today!")

    # Banner Image
    image_path = "assets/banner.png"
    if os.path.exists(image_path):
        st.image(image_path, width=800, caption="Empowering Women, One Ride at a Time")
    else:
        st.warning("Banner image not found! Please check the file path.")

    if st.button("Book a Ride"):
        st.session_state["page"] = "Booking"

def auth_page():
    st.title("User Authentication")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login Successful!")
            st.session_state["page"] = "Home"
        else:
            st.error("Invalid username or password")

def booking_page():
    st.title("Book Your Ride")
    destination = st.text_input("Enter Destination")
    if st.button("Confirm Ride"):
        process_payment()
        st.success("Ride Confirmed! Payment Processed.")

def main():
    st.set_page_config(page_title='SHE - Women Only Ride-Hailing', page_icon='🚗', layout='wide')

    if "page" not in st.session_state:
        st.session_state["page"] = "Landing"

    if st.session_state["page"] == "Landing":
        landing_page()
    elif st.session_state["page"] == "Auth":
        auth_page()
    elif st.session_state["page"] == "Home":
        home_page()
    elif st.session_state["page"] == "Booking":
        booking_page()

if __name__ == "__main__":
    main()
