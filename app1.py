import streamlit as st
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt

def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred) ** 2))

# Load the trained model and scaler
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Title
st.title("Dynamic Ride Price Prediction")
st.write("Enter ride details to predict the dynamically adjusted ride cost.")

# Input fields
number_of_riders = st.slider("Number of Riders", min_value=1, max_value=100, value=50)
number_of_drivers = st.slider("Number of Drivers", min_value=1, max_value=100, value=25)
ride_duration = st.slider("Expected Ride Duration (in mins)", 1, 120, 10)
vehicle_type = st.selectbox("Vehicle Type", ['Economy', 'Premium'])

# Convert categorical to numeric
vehicle_type_numeric = 1 if vehicle_type == 'Premium' else 0

#division features
a,b,c=-1.58274467e-04, 3.66151219e-02,1.53967982e+00
poly = np.poly1d([a, b, c])

if number_of_drivers == 0:
    interpolated_division = 0  # Prevent division by zero
else:
    ratio = number_of_riders / number_of_drivers
    interpolated_division = poly(ratio)


#inputs
input_features = np.array([[number_of_riders,
                            number_of_drivers,
                            ride_duration,
                            vehicle_type_numeric,
                            interpolated_division
                            ]])

# Scale
input_scaled = scaler.transform(input_features)

# Predict
if st.button("Predict Ride Price"):
    log_prediction = model.predict(input_scaled)[0]
    predicted_price = np.expm1(log_prediction)
    st.success(f"Estimated Ride Cost: ₹{predicted_price:.2f}")

