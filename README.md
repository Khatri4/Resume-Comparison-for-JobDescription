# 📄 Resume Comparison ATS System

Welcome to the **Resume Comparison ATS System**! 🎯 This tool is designed to help recruiters and hiring managers quickly assess multiple resumes against a job description using the power of AI. By uploading PDF resumes, you can get an **automated evaluation** of each candidate’s suitability for the role.

## 🛠️ Features
- **AI-Powered Evaluation**: Uses Google’s Gemini Model to compare resumes with the provided job description.
- **PDF Parsing**: Automatically extracts and processes the text from uploaded resumes in PDF format.
- **Match Percentage**: Calculates a match percentage (0-100%) for each candidate based on how well they meet the job requirements.
- **Strengths & Weaknesses**: Provides insights into each candidate’s strengths and weaknesses.
- **Summary Table**: View a sortable table showing the match percentages of all candidates.
- **Best Candidate**: Highlights the most suitable candidate based on the highest match percentage.

## 💻 Technologies Used
- **Python**: The core programming language used to build the app.
- **Streamlit**: Provides the interactive web interface to upload resumes and display results.
- **Google Gemini AI (Generative AI)**: Used to generate match percentages and evaluate resumes.
- **PyPDF2**: For extracting text from PDF files.
- **Pandas**: To handle and display data in a tabular format.
- **dotenv**: Manages environment variables like API keys.

## 🚀 How It Works
1. **Upload Resumes**: Upload multiple PDF resumes via the web interface.
2. **Provide Job Description**: Enter the job description in the text area.
3. **Compare Resumes**: Click the "Compare resumes for the job description" button to get AI-generated results.
4. **View Results**: See match percentages, strengths, weaknesses, and the top candidate in the results section.

## 📝 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Khatri4/resume-comparison-ats.git
cd resume-comparison-ats
```

### 2. Install Dependencies
Make sure you have Python installed. Then, install the required packages by running:
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
This project uses **Google Gemini AI** for generating resume evaluations. You need to configure your own API key.
- Create a `.env` file in the root of the project.
- Add your Google API Key like this:
  ```plaintext
  GOOGLE_API_KEY=your_google_api_key_here
  ```
> 🔑 **Important**: You must use your own API key!

### 4. Run the Application
```bash
streamlit run resume_comparison.py
```

Once the app starts, you can access it via your web browser at `http://localhost:8501`.

## 📂 Project Structure
```
├── .env
├── resume_comparison.py        # Main application file
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## ⚠️ Important Notes
- Ensure your `.env` file is correctly set up with your **Google API Key** for the Gemini AI model.
- This app currently supports only **PDF** resume files.

## 📊 Future Enhancements
- Support for other file formats (e.g., Word, TXT).
- More detailed analysis of resume sections (e.g., skills, education, experience).
- Improved UX with customizable criteria for matching.

