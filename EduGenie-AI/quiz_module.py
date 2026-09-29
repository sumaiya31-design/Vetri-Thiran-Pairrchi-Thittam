from gemini_client import generate_text


def generate_quiz(
    topic: str,
    level: str = "beginner",
    num_questions: int = 3
):
    prompt = f"""
Create a multiple-choice quiz for a student.

Topic: {topic}
Difficulty level: {level}
Number of questions: {num_questions}

For each question provide:
- Question
- Exactly 4 answer options
- The correct answer
- A short explanation

Return the quiz in a clear, numbered format.
"""

    return generate_text(prompt)