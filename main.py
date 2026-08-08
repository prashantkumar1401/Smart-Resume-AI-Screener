import io
import os
from typing import Any

import PyPDF2
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from openai import OpenAI

load_dotenv()

app = FastAPI(
    title="SmartResume AI Screener",
    description="AI-assisted resume screening and job matching API.",
    version="1.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

ALLOWED_EXTENSIONS = {".pdf"}
MAX_FILE_SIZE = 5 * 1024 * 1024


def extract_pdf_text(contents: bytes) -> str:
    """Extract text from a PDF byte stream."""
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(contents))
        pages = []
        for page in reader.pages:
            text = page.extract_text() or ""
            if text.strip():
                pages.append(text.strip())
        return "\n\n".join(pages).strip()
    except Exception as exc:
        raise ValueError("Unable to read the uploaded PDF.") from exc


def build_screening_prompt(job_description: str, resume_text: str) -> str:
    """Build a bounded prompt for the LLM screening step."""
    return f"""
You are an AI resume screening assistant.

Analyze the candidate only against the supplied job description and resume.
Return concise sections:
1. Overall fit score (0-100)
2. Matching skills
3. Missing or weak skills
4. Relevant strengths
5. Potential concerns
6. Recommended next steps

Do not invent experience, qualifications, employers, metrics, or skills.
The score is an AI-generated screening aid and is not a validated hiring assessment.

JOB DESCRIPTION:
{job_description[:12000]}

RESUME:
{resume_text[:20000]}
"""


def analyze_with_llm(job_description: str, resume_text: str) -> str:
    """Generate screening feedback using the configured OpenAI API."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    client = OpenAI(api_key=api_key)
    prompt = build_screening_prompt(job_description, resume_text)

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": "You are a careful HR screening assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=900,
    )

    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("The AI service returned an empty response.")
    return content.strip()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request) -> Any:
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze/", response_class=HTMLResponse)
async def analyze_resume(
    request: Request,
    file: UploadFile = File(...),
    job_description: str = Form(...),
) -> Any:
    filename = (file.filename or "").lower()
    extension = os.path.splitext(filename)[1]

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Only PDF resumes are supported currently.")

    if not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")

    contents = await file.read()
    if not contents:
        raise HTTPException(status_code=400, detail="The uploaded file is empty.")
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="PDF must be 5 MB or smaller.")

    try:
        resume_text = extract_pdf_text(contents)
        if not resume_text:
            raise HTTPException(status_code=400, detail="No extractable text was found in the PDF.")

        analysis = analyze_with_llm(job_description, resume_text)
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "result": analysis},
        )
    except HTTPException:
        raise
    except (RuntimeError, ValueError) as exc:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "result": f"Unable to analyze the resume: {exc}"},
            status_code=500,
        )
    except Exception:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "result": "An unexpected error occurred while analyzing the resume."},
            status_code=500,
        )
