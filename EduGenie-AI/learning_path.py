from gemini_client import generate_text


def recommend_learning_path(
    topic: str,
    level: str = "beginner",
    weeks: int = 4,
    goal: str = ""
) -> str:

    prompt = f"""
Create a personalized learning path for a student.

Topic: {topic}
Student level: {level}
Learning goal: {goal}
Number of weeks: {weeks}

Create a practical step-by-step learning plan.

Include:
1. Learning objectives
2. Recommended topics in order
3. Weekly study plan
4. Practice activities
5. Suggested checkpoints

Keep the plan clear, realistic, and student-friendly.
"""

    return generate_text(prompt)