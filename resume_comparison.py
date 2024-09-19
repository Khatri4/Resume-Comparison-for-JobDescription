from dotenv import load_dotenv
import streamlit as st
import os
import PyPDF2
import google.generativeai as genai
import re
import io
import pandas as pd

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input, pdf_text, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, pdf_text, prompt])
    return response.text

def extract_name_from_pdf(pdf_text):
    lines = pdf_text.split('\n')
    for line in lines[:10]:  # Check first 10 lines
        if line.strip() and not any(word in line.lower() for word in ['resume', 'cv', 'curriculum vitae']):
            return line.strip()
    return "Unknown"  # Return "Unknown" if no name is found

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        pdf_text = ""
        for page_num in range(len(pdf_reader.pages)):
            pdf_text += pdf_reader.pages[page_num].extract_text()

        if pdf_text:
            return pdf_text
        else:
            raise ValueError("No text could be extracted from the PDF.")
    else:
        raise FileNotFoundError("No file uploaded")

def extract_match_percentage(response):
    match = re.search(r'Match Percentage:\s*(\d+)%', response, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return 0  # Default to 0 if no percentage found

st.set_page_config(page_icon="RESUME ATS")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description", key='input')
uploaded_files = st.file_uploader("Upload your resumes", type=['pdf'], accept_multiple_files=True)

if uploaded_files:
    st.write(f"{len(uploaded_files)} resumes uploaded successfully")

submit_compare = st.button("Compare resumes for the job description")

input_prompt_compare = '''
You are an experienced HR with technical expertise in the fields of Data Science, Full Stack Development,
Web Development, Artificial Intelligence, Machine Learning, Generative AI, Data Engineering, UI/UX, App Development,
DevOps, and Data Analysis. Your task is to review the resume provided and compare it against the provided job description.

Evaluate how well this candidate matches the job requirements and provide a match percentage (0-100%).

Your response should include:
1. The calculated match percentage (0-100%) for this candidate.
2. A brief summary of why this candidate is or isn't a good fit for the role.
3. Key strengths and weaknesses of the candidate in relation to the job description.

Respond in the following format:
Match Percentage: X%
Summary: [Your summary here]
Strengths: [List key strengths]
Weaknesses: [List key weaknesses]
'''

if submit_compare and uploaded_files:
    candidate_evaluations = []
    
    for uploaded_file in uploaded_files:
        pdf_text = input_pdf_setup(uploaded_file=uploaded_file)
        candidate_name = extract_name_from_pdf(pdf_text)
        response = get_gemini_response(input_prompt_compare, pdf_text, input_text)
        
        match_percentage = extract_match_percentage(response)
        
        candidate_evaluations.append({
            "Candidate Name": candidate_name,
            "Match Percentage": match_percentage,
            "Evaluation": response
        })
    
    # Sort candidates by match percentage in descending order
    candidate_evaluations.sort(key=lambda x: x["Match Percentage"], reverse=True)
    
    # Display results
    st.subheader("Candidate Evaluations:")
    for eval in candidate_evaluations:
        st.write(f"**{eval['Candidate Name']} - Match: {eval['Match Percentage']}%**")
        st.write(eval['Evaluation'])
        st.write("---")
    
    # Create and display a summary table
    summary_df = pd.DataFrame(candidate_evaluations)[["Candidate Name", "Match Percentage"]]
    st.subheader("Summary Table:")
    st.table(summary_df)
    
    st.subheader("Best Candidate:")
    st.write(f"The most suitable candidate is **{candidate_evaluations[0]['Candidate Name']}** with a match percentage of {candidate_evaluations[0]['Match Percentage']}%.")
else:
    st.write("Please upload the resumes and provide a job description.")
