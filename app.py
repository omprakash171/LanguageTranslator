import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key = api_key)


def language_translator(user_prompt):
    response = client.models.generate_content(
        model = "gemini-2.5-flash", 
        contents = user_prompt
    )
    return response

output = language_translator("Translate this to Hindi: 'Welcome to the course Building LLM Applications'")
print(output.text)