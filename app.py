import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

languages = {
    "Hindi": "Translate the given sentence into Hindi.",
    "Telugu": "Translate the given sentence into Telugu.",
    "French": "Translate the given sentence into French."
}

def language_translator(user_prompt, language):
    system_prompt = languages[language]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt, 
            temperature=0.3, 
            max_output_tokens=2000
        ),
        contents=user_prompt
    )
    return response.text
sentence = "Welcome to the course Building LLM Applications"
language = "Hindi"

output = language_translator(sentence, language)
print(output)