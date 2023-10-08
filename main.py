# Import necessary libraries
import streamlit as st
from prediction import predict_stock  # Import the predict_stock function from prediction.py

# Set the title of the Streamlit app
st.title("Stock Price Predictor")

# Create input fields for user to enter stock data
open_price = st.number_input("Open Price:", step=0.01)  # Input for Open Price
high_price = st.number_input("High Price:", step=0.01)  # Input for High Price
low_price = st.number_input("Low Price:", step=0.01)  # Input for Low Price
volume = st.number_input("Volume:", step=0.01)  # Input for Volume

# Check if the "Predict" button is clicked
if st.button("Predict"):
    # Call the predict_stock function to get the future stock price
    future_price = predict_stock(open_price, high_price, low_price, volume)
    
    # Display the predicted future stock price
    st.write(future_price)
