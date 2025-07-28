import pickle
import numpy as np
import streamlit as st

workclass = {'Federal-gov': 0, 'Local-gov': 1, 'Never-worked': 2, 'Private': 3, 'Self-emp-inc': 4, 'Self-emp-not-inc': 5, 'State-gov': 6, 'Without-pay': 7}

education = {'10th': 0, '11th': 1, '12th': 2, '1st-4th': 3, '5th-6th': 4, '7th-8th': 5, '9th': 6, 'Assoc-acdm': 7, 'Assoc-voc': 8, 'Bachelors': 9, 'Doctorate': 10, 'HS-grad': 11, 'Masters': 12, 'Preschool': 13, 'Prof-school': 14, 'Some-college': 15}

marital_status = {'Divorced': 0, 'Married-AF-spouse': 1, 'Married-civ-spouse': 2, 'Married-spouse-absent': 3, 'Never-married': 4, 'Separated': 5, 'Widowed': 6}

occupation = {'Adm-clerical': 0, 'Armed-Forces': 1, 'Craft-repair': 2, 'Exec-managerial': 3, 'Farming-fishing': 4, 'Handlers-cleaners': 5, 'Machine-op-inspct': 6, 'Other-service': 7, 'Priv-house-serv': 8, 'Prof-specialty': 9, 'Protective-serv': 10, 'Sales': 11, 'Tech-support': 12, 'Transport-moving': 13}

relationship = {'Husband': 0, 'Not-in-family': 1, 'Other-relative': 2, 'Own-child': 3, 'Unmarried': 4, 'Wife': 5}

race = {'Amer-Indian-Eskimo': 0, 'Asian-Pac-Islander': 1, 'Black': 2, 'Other': 3, 'White': 4}

gender = {'Female': 0, 'Male': 1}

native_country = {'Cambodia': 0, 'Canada': 1, 'China': 2, 'Columbia': 3, 'Cuba': 4, 'Dominican-Republic': 5, 'Ecuador': 6, 'El-Salvador': 7, 'England': 8, 'France': 9, 'Germany': 10, 'Greece': 11, 'Guatemala': 12, 'Haiti': 13, 'Holand-Netherlands': 14, 'Honduras': 15, 'Hong': 16, 'Hungary': 17, 'India': 18, 'Iran': 19, 'Ireland': 20, 'Italy': 21, 'Jamaica': 22, 'Japan': 23, 'Laos': 24, 'Mexico': 25, 'Nicaragua': 26, 'Outlying-US(Guam-USVI-etc)': 27, 'Peru': 28, 'Philippines': 29, 'Poland': 30, 'Portugal': 31, 'Puerto-Rico': 32, 'Scotland': 33, 'South': 34, 'Taiwan': 35, 'Thailand': 36, 'Trinadad&Tobago': 37, 'United-States': 38, 'Vietnam': 39, 'Yugoslavia': 40}

income = {0:'<=50K', 1:'>50K'}


with open("Data_Science/Income_Prediction/model.pkl","rb") as p:
    model = pickle.load(p)

st.title("Annual Income Prediction")

st.write ("Please Enter the required Values to predict the Annual Income")

list1 = list(set(workclass.keys()))
list2 = list(set(education.keys()))
list3 = list(set(marital_status.keys()))
list4 = list(set(occupation.keys()))
list5 = list(set(relationship.keys()))
list6 = list(set(race.keys()))
list7 = list(set(gender.keys()))
list8 = list(set(native_country.keys()))

Age = st.number_input("Enter your Age: ", min_value=0)
Workclass = st.selectbox("Select your Workclass:", list1)
Fnlwgt = st.number_input("Fnlwgt:", min_value = 0)
Education = st.selectbox("Select your Education:", list2)
Educational_num = st.number_input("Enter Educational_num:", min_value = 0)
Marital_status = st.selectbox("Select your Marital-status:", list3)
Occupation = st.selectbox("Select Your Occupation:", list4)
Relationship = st.selectbox("Select your relationship:", list5)
Race = st.selectbox("Select Race:", list6)
Gender = st.selectbox("Select Gender:", list7)
Capital_gain = st.number_input("Enter the Value for Capital -gain:",min_value=0)
Capital_loss= st.number_input("Enter how much your Capital-loss:",min_value=0)
HPW = st.number_input("Enter how many hours you work per week:",min_value=0)
Native_country= st.selectbox("Select your Native country:", list8)
             

if st.button("Predict Income"):
    
    wrkc = workclass[Workclass]
    edu = education[Education]
    mrts = marital_status[Marital_status]
    oc = occupation[Occupation]
    rl = relationship[Relationship]
    rc = race[Race]
    gd = gender[Gender]
    nc = native_country[Native_country]
    
    features = np.array([[Age,wrkc,Fnlwgt,edu,Educational_num,mrts,oc,rl,rc,gd,Capital_gain,Capital_loss,HPW,nc]])
    predictions = model.predict(features)[0]
    pred_in_string = income[predictions]
    st.success(f"Your Predicted income is : {predictions:}")
    