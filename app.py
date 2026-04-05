import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

st.title("🏠 House Price Prediction")

st.write("Enter values:")

f1 = st.number_input("Feature 1")
f2 = st.number_input("Feature 2")
f3 = st.number_input("Feature 3")

if st.button("Predict"):
    prediction = model.predict([[f1, f2, f3]])
    st.success(f"Predicted Price: {prediction[0]}")
