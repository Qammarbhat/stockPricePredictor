import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

train_data = pd.read_csv("example_data.csv")

X = train_data[["open_price","high_price","low_price","volume"]]
y = train_data["predicted_high_price"]

model = LinearRegression()
model.fit(X, y)
joblib.dump(model, "pre_trained_model")


def predict_stock_price(open_price, high_price, low_price, volume):
    input_features = [[open_price, high_price, low_price, volume]]
    prediction = model.predict(input_features)
    return prediction[0]