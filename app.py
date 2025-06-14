import streamlit as st 
import re
import pdfplumber
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

st.title("Resume Keyword Scanner")

st.header("Resume")
uploaded_resume_file = st.file_uploader("Upload your resume", type=['pdf', 'txt'])

st.header("Job Description")
uploaded_jd_file = st.file_uploader("Upload job description", type=['pdf', 'txt'])

if st.button("Check Match"):
    if uploaded_resume_file and uploaded_jd_file:
        if uploaded_resume_file.name.endswith('.pdf'):
            resume = extract_text_from_pdf(uploaded_resume_file)
        else:
            resume = uploaded_resume_file.read().decode("utf-8")

        if uploaded_jd_file.name.endswith('.pdf'):
            jd = extract_text_from_pdf(uploaded_jd_file)
        else:
            jd = uploaded_jd_file.read().decode("utf-8")
        
        resume_words = [word for word in re.findall(r'\b\w+\b',resume.lower()) if word not in stop_words]
        jd_words = [word for word in re.findall(r'\b\w+\b',jd.lower()) if word not in stop_words]
        resume_words = [word for word in resume_words if len(word) > 2]
        jd_words = [word for word in jd_words if len(word) > 2]
        resume_set = set(resume_words)
        jd_set = set(jd_words)
        matched = resume_set & jd_set
        missing = jd_set - resume_set
        st.header("Matched")
        st.write(', '.join(sorted(matched)))
        st.header("Missing")
        st.write(', '.join(sorted(missing)))
        match_per = (len(matched)/len(jd_set))*100 
        st.header("Match Percentage")
        st.write(f"{match_per:.2f}%")
    

