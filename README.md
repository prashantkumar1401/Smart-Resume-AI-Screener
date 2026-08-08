# SmartResume AI Screener

An AI-assisted resume screening and job-matching application built with Python and FastAPI. The application accepts a resume and job description, extracts resume text, and uses an LLM to provide structured screening feedback.

> **Portfolio status:** Entry-level AI/software engineering project. Claims in this README describe the implemented project scope and are intentionally kept conservative.

## ✨ Features

- Upload PDF resumes
- Extract text from PDF files
- Accept a job description
- Generate AI-assisted candidate feedback
- Return strengths, concerns and a score out of 100
- Web interface served by FastAPI/Jinja2
- Environment-based API key configuration
- CORS middleware for frontend integration

## 🧰 Tech Stack

- Python
- FastAPI
- OpenAI API
- PyPDF2
- Jinja2
- python-dotenv
- Uvicorn
- HTML/CSS/JavaScript

## 🏗️ Current Flow

```text
Resume PDF + Job Description
            ↓
       FastAPI endpoint
            ↓
       PDF text extraction
            ↓
       LLM analysis prompt
            ↓
   AI-generated screening feedback
            ↓
        Web result page
```

## 📁 Project Structure

```text
Smart-Resume-AI-Screener/
├── main.py
├── requirements.txt
├── templates/
├── static/
├── .env.example
└── README.md
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/prashantkumar1401/Smart-Resume-AI-Screener.git
cd Smart-Resume-AI-Screener
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create `.env` from `.env.example` and add your own API key:

```env
OPENAI_API_KEY=your_api_key_here
```

Never commit `.env` or an API key to GitHub.

### 5. Start the application

```bash
uvicorn main:app --reload
```

Open the local application at `http://127.0.0.1:8000`.

## 🔌 Main Endpoint

`POST /analyze/`

Inputs:

- `file`: PDF resume
- `job_description`: target job description

The endpoint returns the screening result in the web interface.

## ⚠️ Current Limitations

- The current implementation focuses on PDF resumes.
- AI output depends on the configured LLM API.
- The project does not claim validated ATS accuracy or production deployment.
- Automated skill scoring and deterministic evaluation are planned improvements.

## 🔭 Planned Improvements

- DOCX resume support
- Deterministic skill extraction
- TF-IDF/cosine-similarity job matching
- Matched and missing skills
- Structured JSON API responses
- Pydantic response models
- Unit and integration tests
- Better validation and error handling
- Docker configuration
- CI checks
- Streamlit dashboard

## 📌 Skills Demonstrated

Python • FastAPI • REST API fundamentals • PDF parsing • LLM API integration • Environment configuration • Git/GitHub

## 👤 Author

**Prashant Kumar**

- GitHub: https://github.com/prashantkumar1401
- LinkedIn: https://www.linkedin.com/in/Prashant-Kumar-271b11290
