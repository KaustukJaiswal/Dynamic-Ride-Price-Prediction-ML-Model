# Dynamic-Ride-Price-Prediction-ML-Model
🚗 Dynamic Ride Price Prediction
This project aims to predict the adjusted ride cost in real-time using machine learning techniques based on variables such as number of riders, number of drivers, vehicle type, and expected ride duration. It simulates a pricing engine similar to those used by ride-hailing platforms like Uber or Ola.

📌 Project Overview
As ride-sharing platforms dynamically change prices based on demand and supply, building a predictive pricing model is essential. This model uses regression techniques to estimate the adjusted cost of a ride, enabling platforms to anticipate pricing and balance resources more efficiently.

🧠 Machine Learning Approach
Model Used: RandomForestRegressor

Target Variable: adjusted_ride_cost

Input Features:

Number_of_Riders

Number_of_Drivers

Vehicle_Type (encoded as Economy or Premium)

Expected_Ride_Duration

Feature Engineering: Derived non-linear features, polynomial terms, and interactions

Scaling: Input features were scaled using StandardScaler

Performance Metrics: RMSE, MAE, R² score

🛠️ Tech Stack
Language: Python 

Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, streamlit

Deployment: Streamlit Web App

🚀 Streamlit Web App
The model is deployed via a user-friendly Streamlit interface where users can input ride details and receive predicted ride costs.

✅ Features:
Input fields for riders, drivers, duration, and vehicle type

Live prediction of ride price

🔮 Future Enhancements
Incorporate real-time traffic and weather data

Add geospatial ride pickup/dropoff coordinates

Incorporate real-time price prediction based on competitors ride cost
