# 📝 Smart ATS - Resume Analyzer

Smart ATS is an AI-powered resume analysis tool that evaluates resumes against job descriptions to provide insights such as match percentage, missing keywords, and formatting feedback.

## 🚀 Features

- 📄 **Resume Evaluation**: Analyzes resumes and provides a match score based on the job description.
- 🔍 **Keyword Analysis**: Identifies missing skills and suggests improvements.
- 🏗 **Formatting Feedback**: Provides structural and readability feedback.
- 📊 **Match Percentage**: Gives a numerical match score between resume and job description.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Google Gemini AI API
- **Libraries Used**:
  - `streamlit`
  - `PyPDF2`
  - `google-generativeai`
  - `dotenv`
  - `os`

## 📦 Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/smart-ats.git
   cd smart-ats
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Create a `.env` file in the root directory.
   - Add your API key:

     ```sh
     GOOGLE_API_KEY=your_api_key_here
     ```

4. Run the application:

   ```sh
   streamlit run app.py
   ```

## 🎯 How to Use

1. Paste the **Job Description** in the input box.
2. Upload a **PDF resume**.
3. Click on:
   - **Evaluate Resume** to get a detailed analysis.
   - **Check Formatting** to get structural feedback.
   - **Get Match Percentage** to see the match score.

## 📸 Screenshot

<p align="center">
  <img src="https://github.com/user-attachments/assets/dd6b7d0a-ac66-43bb-a6b6-65325315d4dc" alt="Smart ATS UI" width="700" height="600">
</p>
