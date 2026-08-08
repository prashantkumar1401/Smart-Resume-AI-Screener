from fastapi.testclient import TestClient

from main import app, build_screening_prompt, extract_pdf_text

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_empty_job_description_is_rejected():
    response = client.post(
        "/analyze/",
        files={"file": ("resume.pdf", b"not-a-real-pdf", "application/pdf")},
        data={"job_description": "   "},
    )
    assert response.status_code == 400


def test_non_pdf_is_rejected():
    response = client.post(
        "/analyze/",
        files={"file": ("resume.txt", b"resume", "text/plain")},
        data={"job_description": "Python developer"},
    )
    assert response.status_code == 400


def test_prompt_contains_inputs():
    prompt = build_screening_prompt("Python developer", "Python, SQL")
    assert "Python developer" in prompt
    assert "Python, SQL" in prompt
    assert "Do not invent" in prompt


def test_invalid_pdf_raises_value_error():
    try:
        extract_pdf_text(b"not-a-pdf")
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert "Unable to read" in str(exc)
