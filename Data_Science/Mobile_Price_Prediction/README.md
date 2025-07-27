# 📱 Mobile Price Prediction App

This Streamlit web app predicts the launch price of a mobile phone in five countries (India, Pakistan, China, USA, and Dubai) based on its technical specifications. Each country has its own trained machine learning model to ensure accurate predictions based on regional pricing trends.

---

## 🚀 Features

- Predicts mobile prices based on:
  - Brand and model
  - Weight
  - RAM
  - Front and back camera size
  - Processor
  - Battery capacity
  - Screen size
  - Launch year
- Country-specific pricing with 5 separate ML models
- Interactive and responsive UI using **Streamlit**

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – for building the web app
- **NumPy** – for feature array creation
- **Pickle** – for loading serialized models
- **scikit-learn** – (used during model training)

---

## 📦 Folder Structure (Expected)

mobile-price-predictor/
├── app.py
├── README.md
├── requirements.txt
├── Launched Price (India).pkl
├── Launched Price (Pakistan).pkl
├── Launched Price (China).pkl
├── Launched Price (USA).pkl
└── Launched Price (Dubai).pkl

> Also include encoding dictionaries (company, modelN, processor, etc.) either inside `app.py` or as separate `.pkl` files.

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   
   git clone https://github.com/your-username/mobile-price-predictor.git
   cd mobile-price-predictor
