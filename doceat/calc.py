import streamlit as st

st.title("Simple Calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate"):

    if operation == "Addition":
        result = a + b

    elif operation == "Subtraction":
        result = a - b

    elif operation == "Multiplication":
        result = a * b

    elif operation == "Division":
        if b == 0:
            st.error("Cannot divide by zero")
        else:
            result = a / b

    st.success(f"Result: {result}")

    