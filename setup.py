import os
from dotenv import load_dotenv

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".env"))
print("Looking for .env at:", dotenv_path)

load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("OPENAI_API_KEY")
print("API Key Loaded?", api_key is not None)
if api_key:
    print("Key starts with:", api_key[:5])
