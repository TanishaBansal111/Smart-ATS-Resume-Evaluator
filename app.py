import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()  # Load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Templates
input_prompt1 = """
Act as a highly intelligent and skilled ATS (Applicant Tracking System) with expertise in analyzing and evaluating resumes specifically for tech-related fields such as Software Engineering, Data Science, Data Analytics, and Big Data Engineering. 

Your role is to:

1. Evaluate the given resume based on the provided job description.
2. Provide a **detailed percentage match score** between the resume and the job description.
3. Highlight all **missing or relevant keywords** that are important for the role but are not present in the resume.
4. Suggest **specific ways to improve the resume**, such as:
   - Adding relevant technical skills, tools, or programming languages.
   - Improving the structure or phrasing of achievements to align with the job description.
   - Adding measurable impacts and quantifiable achievements where possible.

Consider the following when evaluating:
- Skills, tools, and technologies explicitly mentioned in the job description.
- Job responsibilities and how well the candidate's experience aligns.
- Use of action verbs and result-oriented phrases in the resume.
- Formatting, clarity, and relevance of information.

Provide your feedback in a structured format:
1. **Match Score**: X%
2. **Missing Keywords**: [List of missing skills/tools/technologies]
3. **Suggestions for Improvement**:
   - Specific skills or tools to add.
   - Ways to better phrase existing experience.
   - Tips for improving clarity or layout.

Be concise but detailed, ensuring the feedback is actionable and directly relevant to the role. Use bullet points for clarity.

Resume Content:
{text}

Job Description:
{jd}
"""

input_prompt2 = """
You are a technical recruiter. Please evaluate the resume based on its structure, formatting, and technical relevance to the job description provided. Focus on readability, impact, and completeness of information.
"""

input_prompt3 = """
You are a percentage evaluator system. Provide only the match percentage between the resume and the job description along with a short summary of the alignment.
"""

# Streamlit App
st.title("Smart ATS")
st.text("Improve Your Resume with an ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf", help="Please upload a PDF file.")

col1, col2, col3 = st.columns(3)

with col1:
    submit1 = st.button("Evaluate Resume")
with col2:
    submit2 = st.button("Check Formatting")
with col3:
    submit3 = st.button("Get Match Percentage")

if uploaded_file is not None:
    resume_text = input_pdf_text(uploaded_file)
    if submit1:
        final_prompt = input_prompt1.format(text=resume_text, jd=jd)
        response = get_gemini_response(final_prompt)
        st.subheader("Resume Evaluation")
        st.write(response)
    elif submit2:
        final_prompt = input_prompt2.format(text=resume_text, jd=jd)
        response = get_gemini_response(final_prompt)
        st.subheader("Formatting Feedback")
        st.write(response)
    elif submit3:
        final_prompt = input_prompt3.format(text=resume_text, jd=jd)
        response = get_gemini_response(final_prompt)
        st.subheader("Match Percentage")
        st.write(response)
else:
    st.warning("Please upload a resume file to proceed.")
