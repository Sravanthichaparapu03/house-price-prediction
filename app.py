import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("🏠 California House Price Prediction")

MedInc = st.number_input("Median Income")
HouseAge = st.number_input("House Age")
AveRooms = st.number_input("Average Rooms")
AveBedrms = st.number_input("Average Bedrooms")
Population = st.number_input("Population")
AveOccup = st.number_input("Average Occupancy")
Latitude = st.number_input("Latitude")
Longitude = st.number_input("Longitude")

if st.button("Predict"):
    features = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
    
    scaled_features = scaler.transform(features)  # 🔥 important
    
    prediction = model.predict(scaled_features)
    
    st.success(f"Predicted House Price: {prediction[0]}")
