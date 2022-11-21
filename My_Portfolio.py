import pandas as pd
import streamlit as st
from PIL import Image

st.markdown("<h2 style='text-align: left; color: black;'>About me</h2>", unsafe_allow_html=True)

image_cv = Image.open('8_Pictures/director_picto.png')
image_cv = image_cv#.resize((150, 150))

col1, col2= st.columns(2)    
    with col1:
        st.empty()
    with col2:
        date_range = st.slider('Choose the year interval:', 1900, 2022, value = (1990, 2000))
