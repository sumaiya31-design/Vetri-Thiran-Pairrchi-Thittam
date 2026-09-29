from google import genai
from google.genai import types
import time

from config import GEMINI_API_KEY, GEMINI_MODEL


class GeminiConfigurationError(Exception):
    """Raised when Gemini is not configured correctly."""


class GeminiGenerationError(Exception):
    """Raised when Gemini fails to generate a response."""


def get_client():
    if not GEMINI_API_KEY:
        raise GeminiConfigurationError(
            "GEMINI_API_KEY is not configured."
        )

    return genai.Client(api_key=GEMINI_API_KEY)


def generate_text(prompt: str) -> str:
    client = get_client()

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "You are EduGenie, a helpful educational learning assistant. "
                        "Give clear, accurate, student-friendly explanations."
                    )
                ),
            )

            if not response.text:
                raise GeminiGenerationError(
                    "Gemini returned an empty response."
                )

            return response.text.strip()

        except Exception as exc:
            if attempt < 2:
                time.sleep(2)
            else:
                raise GeminiGenerationError(
                    f"Gemini generation failed: {exc}"
                ) from exc