import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model("Data_Science/Pneumonia_Disease_Prediction_using_CNN/Pneumonia pred Model.keras")

class_name = ["Normal", "Pneumonia"]

st.title("Pneumonia Detection From chest X-Ray")
st.write("Upload a chest X-Ray image to predict whether it shows signs of pneumonia disease")

upload_file = st.file_uploader("Choose an X-Ray Image", type=["jpg","png","jpeg"])

if upload_file is not None:
    img = Image.open(upload_file).convert("RGB")
    st.image(img,caption="Image Uploaded Successfully", use_column_width= True)

    #Preprocessing
    img = img.resize((32,32))
    img_array = image.img_to_array(img)/255.0
    img_array = np.expand_dims(img_array,axis=0) #adding 1 dimenstions

    prediction = model.predict(img_array)
    confidence = float(prediction[0][0])

    if confidence >= 0.5:
        st.error("prediction: Pneumonia Detected")
    else:
        st.success("prediction: No Pneumonia Detected")



