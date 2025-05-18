import streamlit as st

def main():
    st.title("Contact Us")
    st.write("Have questions or feedback? Reach out to us!")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Send"):
        if name and email and message:
            st.success("Thank you for contacting us!")
            # Here you can add backend email sending or database saving
        else:
            st.error("Please fill in all fields.")

if __name__ == "__main__":
    main()
