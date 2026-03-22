
# 🚀 SmartResume-AI-Screener

**SmartResume-AI-Screener** is an LLM-powered, AI-driven resume screening API built with **FastAPI**, **LangChain**, and **OpenAI**. It enables recruiters and hiring platforms to intelligently parse, evaluate, and rank resumes using dynamic, role-specific screening logic — all served through a scalable, production-ready backend.

---

## 🔍 Overview

This system automates resume screening by:
- Extracting and analyzing core resume data (skills, experience, education).
- Using GPT-powered evaluations to score and rank candidates based on a given job description.
- Offering flexible param-based filtering for UI integrations.
- Supporting multi-format resume inputs (PDF, DOCX).

Designed for real-world hiring workflows and easy deployment using Docker + CI/CD.

---

## 🧠 Features

- ✅ **LLM-Powered Scoring** using GPT via LangChain
- ⚙️ **FastAPI Backend** with modular endpoints
- 📑 **Multi-format Resume Support** (.pdf, .docx)
- 🎯 **Dynamic Role Matching** using job descriptions
- 🔍 **10+ Filter Parameters** for custom screening
- 🐳 **Dockerized for Production**, CI/CD-ready
- 🔐 **Environment Secrets** managed via `.env`

---

## 🛠️ Tech Stack

| Category     | Tools Used                          |
|--------------|-------------------------------------|
| Language     | Python 3.10+                        |
| Backend      | FastAPI                             |
| AI & LLM     | OpenAI GPT-3.5/4, LangChain         |
| Parsing      | pdfminer, docx2txt, spaCy           |
| Containerization | Docker, Docker Compose         |
| Deployment   | Render / Vercel / AWS (Optional)    |
| Version Control | Git, GitHub                      |

---

## ⚙️ Getting Started

### 2. Create a Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_key_here
```

> ⚠️ Never commit your `.env` file to GitHub!

---

## ▶️ Running the App

### Local Development (Uvicorn)

```bash
uvicorn main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

---

## 🐳 Docker Deployment

### 1. Build and Run

```bash
docker build -t smartresume-api .
docker run -d -p 8000:8000 smartresume-api
```

---

## 📦 Folder Structure

```bash
SmartResume-AI-Screener/
├── app/
│   ├── main.py
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── routers/
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md
```

---


---

> Made with ❤️ by [Prashant Kumar](https://github.com/prashantkumar1401))
