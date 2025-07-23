# 🚢 Titanic Survival Prediction App

This is a Machine Learning web application built using **Logistic Regression** and **Streamlit** to predict whether a passenger on the Titanic would have survived based on their personal details.

---

## 📌 Features

- Predict survival based on:
  - Passenger class (Pclass)
  - Age
  - Siblings/Spouses aboard (SibSp)
  - Parents/Children aboard (Parch)
  - Fare paid
  - Sex (male/female)
  - Embarkation port (Cherbourg, Queenstown, Southampton)
- Logistic Regression model trained with preprocessed Titanic dataset
- Clean UI using Streamlit
- IQR-based outlier handling for `Age` and `Fare`
- Probability-based survival prediction
- Ready to deploy on **Streamlit Cloud**

---

## 🚀 Live Demo

👉 [Click here to try the app](https://your-streamlit-app-url.streamlit.app)  
*Replace with your actual Streamlit app link*

---

## 🗂 Project Structure
📦 titanic-logistic-app/
├── app.py # Streamlit application
├── Titanic_train.csv # Training dataset
├── requirements.txt # Python dependencies
├── README.md # Project documentation

---

## ⚙️ How to Run Locally

1. Clone the repository:

git clone https://github.com/yourusername/titanic-logistic-app.git
cd titanic-logistic-app

2. Install the dependencies:

pip install -r requirements.txt

3. Run the Streamlit app:

streamlit run app.py

🧠 Model Info - 

Algorithm: Logistic Regression (scikit-learn)
Data: Titanic training dataset
Preprocessing includes:
        -- Handling missing values
        -- Label encoding (Sex, Embarked)
        -- Outlier capping using IQR method

🙋‍♂️ Author
Omkar Patne
📧 omkar2252001@gmail.com
🔗 https://github.com/yourusername