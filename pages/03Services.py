import streamlit as st
from streamlit_lottie import st_lottie
import json

# Function to load Lottie animations from local files
def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading animation from {filepath}: {e}")
        return None
st.title("Our Services")
st.subheader("SHE - Women-Only Ride-Hailing App")
st.markdown("""
SHE offers a safe and secure ride-hailing experience with the following features:
""")

# Load all animations from the local assets folder
safety_animation = load_lottiefile("assets/animations/safety.json")
comfort_animation = load_lottiefile("assets/animations/comfort.json")
tracking_animation = load_lottiefile("assets/animations/tracking.json")
support_animation = load_lottiefile("assets/animations/support.json")

# Display the animations with descriptions
st.markdown("### 🚗 Safety First")
if safety_animation:
    st_lottie(safety_animation, height=250, width=250, key="safety")
st.write("We prioritize your safety with women-only drivers and robust safety protocols.")

st.markdown("### 💺 Comfort")
if comfort_animation:
    st_lottie(comfort_animation, height=250, width=250, key="comfort")
st.write("Experience ultimate comfort with spacious seating and a friendly environment. You can book a ride from the comfort of your home.")

st.markdown("### 🌍 Live Tracking")
if tracking_animation:
    st_lottie(tracking_animation, height=250, width=250, key="tracking")
st.write("Track your ride in real-time and share your location with loved ones.")

st.markdown("### 📞 Support")
if support_animation:
    st_lottie(support_animation, height=250, width=250, key="support")
st.write("Our dedicated support team is available 24/7 to assist you with any concerns.")
