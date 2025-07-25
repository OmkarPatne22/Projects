import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("Data_Science/Titanic_Survival_Pridiction/logistic_model.pkl","rb") as p:
    model = pickle.load(p)

# Streamlit UI
st.set_page_config(page_title="Titanic Survival Predictor", layout="centered")
st.title("🚢 Titanic Survival Predictor")
st.write("Fill in the passenger details below to predict survival.")

# User Inputs
Pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
Age = st.number_input("Age", min_value=0)
SibSp = st.number_input("Number of Siblings/Spouses aboard", min_value=0, max_value=10)
Parch = st.number_input("Number of Parents/Children aboard", min_value=0, max_value=10)
Fare = st.number_input("Fare Paid", min_value=0.0)
Sex_male = st.radio("Sex", ['Male', 'Female']) == 'Male'

# Embarked Port
embarked = st.selectbox("Embarked Port", ["C (Cherbourg)", "Q (Queenstown)", "S (Southampton)"])
Embarked_Q = int(embarked.startswith("Q"))
Embarked_S = int(embarked.startswith("S"))

# Feature Vector
features = np.array([[Pclass, Age, SibSp, Parch, Fare,
                      int(Sex_male), int(Embarked_Q), int(Embarked_S)]])

# Prediction
if st.button("Predict Survival"):
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    if prediction == 1:
        st.success(f"🎉 This passenger would have SURVIVED! (Prob: {probability:.2f})")
    else:
        st.error(f"❌ This passenger would NOT have survived. (Prob: {probability:.2f})")
