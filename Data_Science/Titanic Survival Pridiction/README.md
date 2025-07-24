
# 🚢 Titanic Survival Predictor

This is an **interactive web application** that predicts the survival chances of a Titanic passenger based on their personal and travel details.  
The application uses a **Logistic Regression** model trained on the Titanic dataset and provides both **predicted survival** and the **probability of survival**.

---

## 🌟 About the Project
The sinking of the Titanic is one of the most infamous shipwrecks in history.  
This application allows users to explore how different features such as **class, age, sex, fare**, and **embarkation port** influenced survival chances.

It is built using **Streamlit** for a smooth and interactive experience, making it easy for users to experiment with various passenger profiles.

---

## 🚀 Features
- **Interactive UI:** Select or input passenger details using dropdowns, sliders, and radio buttons.
- **Prediction & Probability:** Provides a survival prediction (Survived/Not Survived) along with the probability score.
- **Logistic Regression Model:** Pre-trained model (`logistic_model.pkl`) based on Titanic dataset.
- **Instant Results:** No waiting—get predictions in real-time.

---

## 🛠️ How It Works
1. Fill in passenger details:
   - Passenger class (1st, 2nd, 3rd)
   - Age
   - Number of siblings/spouses & parents/children aboard
   - Fare paid
   - Gender
   - Port of embarkation (Cherbourg, Queenstown, Southampton)
2. Click on **Predict Survival**.
3. Instantly view the survival prediction and its probability.

---

## 📂 Project Structure
titanic-survival-predictor/
│
├── app.py                  # Streamlit application
├── logistic_model.pkl      # Pre-trained Logistic Regression model
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation

---

## 🧠 The Model
This project uses **Logistic Regression**, a popular algorithm for binary classification tasks.  
- **Input Features:**  
  - Passenger Class (Pclass)  
  - Age  
  - Number of siblings/spouses aboard (SibSp)  
  - Number of parents/children aboard (Parch)  
  - Fare  
  - Gender (Male/Female)  
  - Embarked port (Cherbourg, Queenstown, Southampton)  
- **Output:**  
  - Predicted survival (1 = Survived, 0 = Not Survived)  
  - Probability of survival

---

## 🔧 Installation & Setup
1. **Clone the repository:**
   
   git clone https://github.com/OmkarPatne22/Projects/blob/main/Data_Science/Titanic%20Survival%20Pridiction/app.py

2. **Navigate to the project folder:**
    
   cd titanic-survival-predictor
   
3. **Install dependencies:**
    
   pip install -r requirements.txt

4. **Ensure the model file is present:**  

   The application requires `logistic_model.pkl` (the pre-trained model) to work.

5. **Run the application:**
    
   streamlit run app.py
   
6. **Open your browser:**  
   Go to `http://localhost:8501` to start using the app.

---

## 📦 Requirements
- Python 3.x
- Streamlit
- Pandas
- NumPy
- Pickle

Install all dependencies with:
bash
pip install -r requirements.txt

---

## 🎯 Use Cases
- **Students & Learners:** Understand logistic regression and binary classification in action.
- **Data Science Enthusiasts:** Experiment with Titanic dataset features.
- **Portfolio Project:** Great addition for showcasing skills in Python, Streamlit, and ML.

---

## 🤝 Contributing
Contributions are welcome!  
Feel free to fork this repository, add new features, and submit pull requests.
