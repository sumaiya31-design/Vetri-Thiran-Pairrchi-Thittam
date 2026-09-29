from gemini_client import generate_text


def explain_concept(concept: str) -> str:
    prompt = f"""
Explain the following concept to a student in a clear and easy-to-understand way.

Concept:
{concept}

Use this structure:

1. Simple definition
2. Detailed explanation
3. Real-world example
4. Key points to remember

Avoid unnecessary technical jargon.
"""

    return generate_text(prompt)