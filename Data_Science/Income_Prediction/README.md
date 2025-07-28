# 💰 Annual Income Prediction App

This is a Streamlit-based web application that predicts whether a person earns **more or less than $50K annually**, based on personal and professional details.

## 🚀 About the App

Users input various personal features, and the app predicts income category using a trained machine learning model(Logistic Regression).

## 🖥 Demo UI Features

- Input fields for demographic and employment-related information
- One-click prediction using a trained model
- Categorical options like Workclass, Education, Marital Status, Gender, etc.

## 🔢 Features Used for Prediction

- Age
- Workclass
- Fnlwgt
- Education
- Education-num
- Marital-status
- Occupation
- Relationship
- Race
- Gender
- Capital-gain
- Capital-loss
- Hours-per-week
- Native-country

## 🧪 Tech Stack

- **Python**
- **Streamlit**
- **NumPy**
- **Scikit-learn** (for model training)
- Trained ML model (`model.pkl`) assumed to be loaded

## Requirements

    pandas
    numpy
    scikit-learn
    streamlit
    
## File Structure

income-prediction-app/
│
├── app.py                  # Main Streamlit app
├── model.pkl               # Trained ML model
├── mappings.py             # Dictionary mappings for categories
├── requirements.txt
└── README.md

🧠 Model Info
The model predicts if income is:

<=50K

>50K

Prediction is made based on a features array constructed from the UI inputs.