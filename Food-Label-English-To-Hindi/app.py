### Food Label Translation from English to Hindi using Google Gemini Pro Vision API
from dotenv import load_dotenv

load_dotenv()  # load all the environment variables

import os

import google.generativeai as genai
import streamlit as st
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API And get response
def get_gemini_response(prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if prompt != "":
        response = model.generate_content([prompt, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Translate Food Package Labels From English to Hindi with Google Gemini",
                   page_icon=":fork_and_knife:", layout="wide")

# GitHub link and logo in the sidebar

st.sidebar.markdown(
    """
    <a href="https://github.com/TegveerG/Google-Gemini-Crash-Course/blob/main/Food-Label-English-To-Hindi/app.py">
        <img src="https://badgen.net/badge/icon/GitHub?icon=github&label" width="100">
    </a>
    """,
    unsafe_allow_html=True
)

# Add space

st.sidebar.markdown(
    """

    """
)

# Add food and health-related images
fssai_image = "https://bsmedia.business-standard.com/_media/bs/img/article/2023-04/21/full/1682088340-8915.png?im=FeatureCrop,size=(826,465)"
healthy_food_image = "https://img.freepik.com/free-photo/buddha-bowl-dish-with-vegetables-legumes-top-view_1150-42589.jpg"
unhealthy_food_image = "https://t4.ftcdn.net/jpg/02/86/17/89/360_F_286178925_8zk89O9uC5JJVPvqhvBMUpaRxp8AFXzD.jpg"

st.sidebar.image(fssai_image, use_column_width=True)
st.sidebar.image(healthy_food_image, caption="Healthy Foods/स्वस्थ आहार", use_column_width=True)
st.sidebar.image(unhealthy_food_image, caption="Unhealthy Foods/अस्वस्थ आहार", use_column_width=True)

# Main content of the app
st.title("Translate Food Package Labels From English to Hindi with Google Gemini")
st.header("गूगल जेमिनी के साथ खाद्य पैकेज लेबल्स को अंग्रेजी से हिंदी में अनुवाद करें")
st.markdown("Input food package label image, preferably of both ingredients and nutritional facts. If both do not fit in one image, you can upload ingredients only.")

uploaded_file = st.file_uploader("खाद्य पैकेज लेबल की तस्वीर दर्ज करें, जिसमें मुख्य रूप से सामग्री और पोषण संबंधी जानकारी होनी चाहिए। अगर एक ही तस्वीर में दोनों नहीं आते हैं, तो आप केवल सामग्री वाली तस्वीर अपलोड कर सकते हैं।", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Uploaded Image ↑/आपकी डाली गई चित्र ↑", use_column_width=True)

submit = st.button("Tell me the product details in Hindi/मुझे उत्पाद के विवरण हिंदी में बताएं")

input_prompt = """
You are an expert nutritionist as well as an expert translator between English and Hindi.
You need to read the food label items, including ingredients and nutritional facts, from the image of back packaging food label (mainly in English)
and translate the product details to Hindi.

Output the translation in Hindi of all the following as separate titles in bold like so:

1. सामग्री

Then list the ingredients of the food product below the ingredients title

2. पोषण संबंधी जानकारी

Then list the nutritional details of the food product below the Nutrition details title

3. क्या यह उत्पाद स्वस्थ या अस्वस्थ है

In one to two sentences, describe if the product is healthy or unhealthy.

4. उत्पाद के लिए घर पर पकाया गया स्वस्थ विकल्प

Describe the healthier alternatives to the product provided. If you wish, you can also suggest a healthier dish with similar to the product provided.
"""

# If submit button is clicked
if submit:
    response = get_gemini_response(input_prompt, image)
    st.subheader("The Product Details in Hindi are:/उत्पाद के विवरण हिंदी में:")
    st.write(response)

    # Display the additional image below the product details
    additional_image_url = "https://healthylife.werindia.com/wp-content/uploads/2015/04/Food-Safety-Label.jpg"
    st.image(additional_image_url, caption="FSSAI's Food Label requirements in India/भारत में खाद्य सुरक्षा और मानक प्राधिकृति निगम के खाद्य लेबल आवश्यकताओं", use_column_width=False)

def collect_telemetry_data(text, selected_model, prediction_text):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    telemetry_data[timestamp] = {
        'input_data': text,
        'selected_model': selected_model,
        'prediction_text': prediction_text
    }
    # Save telemetry data to a JSON file with the current date and time as the filename
    filename = f"telemetry_data_{timestamp.replace(' ', '_').replace(':', '-')}.json"
    with open(filename, 'w') as file:
        json.dump(telemetry_data[timestamp], file, indent=4)

def save_telemetry_to_db(text, selected_model, prediction_text):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    telemetry_entry = TelemetryData(
        timestamp=timestamp,
        input_data=text,
        selected_model=selected_model,
        prediction_text=prediction_text
    )
    db.session.add(telemetry_entry)
    db.session.commit()


