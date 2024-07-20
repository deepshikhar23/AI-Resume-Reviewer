import streamlit as st
import os
import PyPDF2 as pdf
import google.generativeai as genai

# Load environment variables from .env file (assuming it's in the same directory)
from dotenv import load_dotenv
load_dotenv(dotenv_path = 'C:/Users/HP/ATSapp/.env')

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)


def gemini_response(input, text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(0,len(reader.pages)):
        page = reader.pages[page]
        text = text + page.extract_text()
    return text


# Streamlit app here

st.title("ATS Resume Scanner")
st.text("Make your resume ATS friendly")
jd = st.text_area("Paste the job description here")
uploaded_file = st.file_uploader("Upload your resume", type="pdf", help="Please upload the pdf")


submit1 = st.button("How is my resume?")
submit2 = st.button("Tell me the keywords that my resume is missing")
submit3 = st.button("Give my resume a matching score out of 10")


if uploaded_file is not None:
    st.write("Resume uploaded successfully")


prompt1 = '''Suppose you are an experienced technical HR manager with 10 years of experience having expertise in resume review specially for the tech 
roles like Data Science, Data Analyst, Full Stack Developer, Devops and Data Engineering. Your task is to review the provided resume against the job 
description. Please share a detailed and honest evaluation on whether the provided resume aligns with the job description with the strengths and
weakness of applicant with respect to the provided job description. Here is the resume: '''

prompt2 = '''Suppose you are an experienced technical HR manager with 10 years of experience having expertise in keyword matching specially for the tech 
roles like Data Science, Data Analyst, Full Stack Developer, Devops and Data Engineering. Your task is to review the provided resume against the job 
description. Please make a list of the most appeared keywords in the job description and check if those keywords are already in resume or not?
If they are in resume, then it's fine otherwise simply return a list of keywords that are in job description but not in resume. Here is the resume: '''

prompt3 = '''Suppose you are an experienced technical HR manager with 10 years of experience having expertise in ATS systems specially for the tech 
roles like Data Science, Data Analyst, Full Stack Developer, Devops and Data Engineering. Your task is to review the provided resume against the job 
description. Please give the provided resume a score out of 10 based on how much it matches or aligns with the provided job description. If it does not
get a 10 simply list out the necessary changes which when made in the resume will make the resume a 10. Here is the resume: '''

if submit1:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = gemini_response(prompt1, text)
        st.subheader(response)
    else:
        st.write("Please upload your resume")

elif submit2:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = gemini_response(prompt2, text)
        st.subheader(response)
    else:
        st.write("Please upload your resume")

elif submit3:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = gemini_response(prompt3, text)
        st.subheader(response)
    else:
        st.write("Please upload your resume")