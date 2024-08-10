import streamlit as st 
import google.generativeai as genai
import os
import PyPDF2 as pdf 

from dotenv import load_dotenv

load_dotenv() ### Load all the environment variables

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

### Gemini Pro Response
def get_gemini_response(input):
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(input)
  return response.text 

def input_pdf_text(upload_file):
  reader = pdf.PdfReader(upload_file)
  text = ""
  for page in range(len(reader.pages)):
    page = reader.pages[page]
    text += str(page.extract_text())
  return text 


## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf")

submit = st.button("Submit")

if submit:
  if uploaded_file is not None:
    text = input_pdf_text(uploaded_file)
    ## Prompt Template
  input_prompt = """
  You have to act like a skilled or very experienced ATS(Application Tracking System)
  with a deep understanding of tech field,software engineering,data science ,data analyst
  and big data engineer. Your task is to evaluate the resume based on the given job   description.
  You must consider that the job market is very competitive and you should provide 
  best assistance for improving the resumes. Assign the percentage Matching based 
  on Jd andthe missing keywords with high accuracy
  resume:{}
  description:{}

  I want the response in one single string having the structure
  {{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
  """.format(text,jd)
  response = get_gemini_response(input_prompt)
  
  st.subheader(response)
    