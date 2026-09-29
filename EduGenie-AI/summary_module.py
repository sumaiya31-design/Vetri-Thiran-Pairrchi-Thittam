from gemini_client import generate_text


def summarize_text(text: str, level: str = "beginner") -> str:
    prompt = f"""
Summarize the following text for a student.

Student level: {level}

Text:
{text}

Create a clear and concise summary.
Include:
1. Main idea
2. Important points
3. Key terms or concepts

Do not add information that is not present in the original text.
"""

    return generate_text(prompt)