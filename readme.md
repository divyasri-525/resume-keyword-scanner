# 📄 Resume Keyword Scanner

A simple Streamlit web app that helps job seekers compare their resume with a job description by scanning for **matching keywords** and calculating the **match percentage**.

## 🔍 Features

- Upload resume and job description files (supports `.pdf` and `.txt`)
- Extracts and cleans text from both files
- Identifies **common (matched)** and **missing keywords**
- Calculates a **match percentage**
- Clean and responsive web interface using Streamlit

## 🚀 Live Demo

[Click here to try the app](https://resume-keyword-scanner-ds-525.streamlit.app/)

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **pdfplumber** (for PDF text extraction)
- **Regular Expressions (re module)**

## 🧾 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/divyasri-525/resume-keyword-scanner

# 2. Navigate to the folder
cd resume-keyword-scanner

# 3. Create and activate a virtual environment (optional but recommended)

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
streamlit run app.py'''
