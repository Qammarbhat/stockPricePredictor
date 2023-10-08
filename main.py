import streamlit as st
from prediction import predict_stock
import langchain
from prediction import predict_stock

st.title("Stock Price Predictor")


# Creating input fields
open_price = st.number_input("Open Price:", step = 0.01)
high_price = st.number_input("High Price:", step = 0.01)
low_price = st.number_input("Low Price:", step = 0.01)
volume = st.number_input("Volume:", step = 0.01)

if st.button("Predict"):
  future_price = predict_stock(open_price, high_price, low_price, volume)
  st.write( future_price) 

