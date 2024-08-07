import streamlit as st

st.title("Calculator")

num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")

operation = st.selectbox("Choose an operation",("Add","Subtract","Multiply","Division"))

if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Division":
    if num2!=0:
        result = num1 / num2
    else:
        result = "Math Error! Division by Zero"

st.write("Result:",result)