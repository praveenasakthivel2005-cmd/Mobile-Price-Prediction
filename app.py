# ----------------
# PAGE SETTINGS
# ----------------

from tkinter import Image

import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# ------------
# LOAD MODEL
# ------------

loaded_model = joblib.load(r"C:/Users/Admin/Desktop/Mobile Price prediction(ML Project)/best_mobile_price_model.pkt")

st.set_page_config(
    page_title="Mobile Price Prediction",
    page_icon="📱",
    layout="centered"
)

# -------
# TITLE
# -------

st.title("Mobile Price Prediction")
st.write("Enter the mobile specifications below"
         "to predict the estimated mobile price.")

# -------
# IMAGE
# -------

image = Image.open(r"C:/Users/Admin/Desktop/Mobile Price prediction(ML Project)/Mobile_image.png")
st.image(
    image,
    caption="Mobile Price Prediction",
    use_container_width=True 
)

# ---------------
# MOBILE DETAILS
# ---------------

st.subheader("Mobile Specifications")

brand = st.selectbox(
    "Select Brand",
    [
        "Samsung",
        "Apple",
        "Redmi",
        "Realme",
        "Vivo",
        "Oppo",
        "Motorola",
        "OnePlus",
    ]
)

ram = st.selectbox(
    "RAM_GB",
     [4,6,8,12,16]
)

storage = st.selectbox(
    "Storage_GB",
    [64,128,256,512]
)

battery = st.selectbox(
    "Battery (mAh)",
    ["3000","3500","4000","4500","5000","5500","6000","6500","7000"]
)

camera = st.selectbox(
    "Camera (MP)",
    [8, 12, 16, 20, 32, 48, 50, 64, 108, 200]
)

year = st.selectbox(
    "Release year",
    [2020,2021,2022,2023,2024,2025,2026],
    index=3
)

# -------------
# PREDICTION
# -------------

if st.button("Predict Mobile Price"):

    new_mobile = pd.DataFrame([{
        "Brand": brand,
        "RAM_GB": ram,
        "Storage_GB": storage,
        "Battery_mAh": battery,
        "Camera_MP": camera,
        "Year": year
    }])

    Predicted_price = loaded_model.predict(new_mobile)[0]

    st.subheader("Prediction Completed!")
    st.subheader("Mobile Details:")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Brand:", brand)
        st.write("RAM:", ram, "GB")
        st.write("Storage:", storage, "GB")

    with col2:
        st.write("Battery:", battery, "mAh")
        st.write("Camera:", camera, "MP")
        st.write("Year:", year)

    st.subheader("Predicted Mobile Price")
    st.success(f"₹{Predicted_price:,.0f}")
    
             
             