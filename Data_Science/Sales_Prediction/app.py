import streamlit as st
import pickle
import numpy as np

with open("Data_Science/Sales_Prediction/model.pkl","rb") as p:
    model = pickle.load(p)

st.title("Sales Prediction Application")

st.write ("Please Enter your Advertisement Invest in each to predict the sales.")

TV = st.number_input("Advertising investment in TV", min_value = 0.0, format = "%.2f")
RADIO = st.number_input("Advertising investment in Radio", min_value = 0.0, format = "%.2f")
NEWSPAPER = st.number_input("Advertising investment in Newspaper", min_value = 0.0, format = "%.2f")

if st.button("Predict Sales"):
    features = np.array([[TV,RADIO,NEWSPAPER]])
    predictions = model.predict(features)[0]
    st.success(f"Predicted Sales: {predictions:.2f}")

    