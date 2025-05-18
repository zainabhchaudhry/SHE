import os
import streamlit as st
import stripe
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch Stripe API key securely
stripe_api_key = os.getenv("STRIPE_API_KEY")

if not stripe_api_key:
    st.error("Stripe API key not found! Please add STRIPE_API_KEY in your .env file.")
    st.stop()

# Initialize Stripe with the API key
stripe.api_key = stripe_api_key

st.title("Dashboard - SHE Ride-Hailing App")
st.write("Welcome to your dashboard. Manage your rides and payments here.")

# Payment Configuration
st.header("Make a Payment")

# Dummy amount for ride payment
ride_amount = 500  # in PKR or your desired currency

st.write(f"Ride Fare: {ride_amount} PKR")

try:
    # Create a Stripe checkout session
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "pkr",
                "product_data": {
                    "name": "SHE Ride Fare",
                },
                "unit_amount": ride_amount * 100,  # amount in smallest currency unit (cents/paise)
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="http://localhost:8501",  # Update to your live URL in production
        cancel_url="http://localhost:8501",
    )

    st.success("Payment Session Created! Click below to pay.")
    st.markdown(f"[Pay Now]({session.url})")

except Exception as e:
    st.error(f"Error creating payment session: {str(e)}")

# Payment Status Section
st.subheader("Payment Status")
st.write("Payment status will be displayed here after processing.")
