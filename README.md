# Language Translator

A Python application that uses Google's Gemini API to translate text between languages.

## Features

- Translate text to different languages using Gemini AI
- Simple and easy-to-use interface
- Powered by Google's Gemini 2.5 Flash model

## Setup

1. Clone this repository
2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`

4. Install dependencies:

   ```bash
   pip install google-genai python-dotenv
   ```

5. Create a `.env` file in the root directory:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

6. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Usage

Run the application:

```bash
python app.py
```

## Example

The default example translates "Welcome to the course Building LLM Applications" to Hindi.

You can modify the `user_input` in `app.py` to translate other texts or to different languages.
