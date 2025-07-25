
# 📊 Sales Prediction App

Welcome to the **Sales Prediction Web Application**!  
This project leverages the power of **Machine Learning** to predict sales based on advertising investments across **TV**, **Radio**, and **Newspaper** channels.  
It is built with **Streamlit** for a smooth, interactive user experience.

---

## 🌟 Why This Project?
Advertising plays a crucial role in driving sales, but how do you know how much impact your investment will make?  
This app provides an **instant, data-driven prediction** for sales based on your advertising budget across three major channels.  
Simply enter your **TV**, **Radio**, and **Newspaper** advertising investments, and the model will instantly provide the **predicted sales value**.

---

## 🚀 Key Features
- **Interactive Web Interface:** Simple, clean, and responsive design powered by Streamlit.
- **Real-Time Predictions:** Get instant results for your inputs without complex setups.
- **Pre-Trained ML Model:** Uses a regression model (stored as `model.pkl`) trained on historical advertising data.
- **Customizable:** Easily extend or retrain the model with new data.

---

## 🛠️ How It Works
1. **Input Your Data:** Enter advertising investment amounts for TV, Radio, and Newspaper.
2. **Run Prediction:** Click the **Predict Sales** button.
3. **Get Results:** Instantly view the predicted sales value based on your inputs.

---

## 📂 Project Structure
sales-prediction-app/
│
├── app.py               # Main Streamlit application
├── model.pkl            # Pre-trained machine learning model
├── requirements.txt     # List of Python dependencies
└── README.md            # Project documentation

---

## 🧠 The Model
The ML model behind this app is trained using Linear regression techniques to forecast sales based on marketing spending.  
- **Input Features:**  
  - TV Advertising Budget (float)  
  - Radio Advertising Budget (float)  
  - Newspaper Advertising Budget (float)  
- **Output:**  
  - Predicted sales (float)

This allows businesses to **estimate ROI** and make more **informed decisions** about their advertising strategies.

---

## 🔧 Installation & Setup
1. **Clone the repository:**
   
   git clone https://github.com/OmkarPatne22/Projects/blob/main/Data_Science/Sales%20Prediction/app.py

2. **Navigate to the project folder:**
   
   cd sales-prediction-app

3. **Install dependencies:**

   pip install -r requirements.txt

4. **Ensure the model file is present:**  
   The application requires `model.pkl` (the pre-trained model) to work.

5. **Run the application:**

   streamlit run app.py

6. **Open your browser:**  
   Go to `http://localhost:8501` to start using the app.
---

## 📦 Requirements
- Python 3.x
- Streamlit
- NumPy
- Pickle

Install all dependencies with:

pip install -r requirements.txt

---

## 🔗 Live Demo 

👉 [**Click here to try the app**](https://salesprice-prediction.streamlit.app/)  

---

## 🎯 Use Cases
- **Marketing Agencies:** Quickly estimate sales impact of ad campaigns.  
- **Business Analysts:** Analyze advertising budgets and optimize spending.  
- **Students & Learners:** A great project to understand regression models and Streamlit.  

---

## 🤝 Contributing
Contributions are always welcome!  
If you’d like to add features or improve the UI, feel free to fork this repository and submit a pull request.
