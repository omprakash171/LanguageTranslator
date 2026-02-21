from google import genai
from dotenv import dotenv_values

config = dotenv_values(".env")
api_key = config['GEMINI_API_KEY']

client = genai.Client(api_key = api_key)


def language_translator(user_input):
    response = client.models.generate_content(
        model = "gemini-2.5-flash", 
        contents = user_input
    )
    return response

output = language_translator("Translate this to Hindi: 'Welcome to the course Building LLM Applications'")
print(output.text)