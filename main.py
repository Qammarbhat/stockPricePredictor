# Import necessary libraries
import streamlit as st
from prediction import predict_stock  # Import the predict_stock function from prediction.py
from prediction_costEff import predict_stock_price

# Set the title of the Streamlit app
st.title("Stock Price Predictor")

# Create input fields for user to enter stock data
open_price = st.number_input("Open Price:", step=0.01)  # Input for Open Price
high_price = st.number_input("High Price:", step=0.01)  # Input for High Price
low_price = st.number_input("Low Price:", step=0.01)  # Input for Low Price
volume = st.number_input("Volume:", step=0.01)  # Input for Volume


train_data ="example_data.csv"
# Check if the "Predict" button is clicked
if st.button("Predict"):
    # Call the predict_stock function to get the future stock price
    future_price = predict_stock_price(open_price, high_price, low_price, volume)
    
    # Display the predicted future stock price
    st.write(
    f"<span style='font-size: 24px; color: black;'>Predicted Future Price: {future_price}</span>",
    unsafe_allow_html=True
)

