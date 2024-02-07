### Food Label Translation from English to Hindi using Google Gemini Pro Vision API
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import os

import google.generativeai as genai
import streamlit as st
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_response(prompt,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if prompt!="":
       response = model.generate_content([prompt,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Translate Food Package Labels From English to Hindi with Google Gemini")

st.title("Translate Food Package Labels From English to Hindi with Google Gemini")
st.header("गूगल जेमिनी के साथ खाद्य पैकेज लेबल्स को अंग्रेजी से हिंदी में अनुवाद करें")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me the product details in Hindi")

input_prompt="""
You are an expert nutritionist as well as an expert translator between English and Hindi.
You need to read the food items (such as ingredients and nutrition) from the image of back packaging food label (mainly in English) and translate the product details to Hindi.
First provide the translation in Hindi of all the following: ingredients, then the nutrition details of the food items, and lastly your verdict on the healthiness of the food product.
"""

## If submit button is clicked

if submit:
    response=get_gemini_response(input_prompt, image)
    st.subheader("The Product Details in Hindi are:")
    st.write(response)