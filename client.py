import google.generativeai as genai
import os

apikey = "AIzaSyAFfFRRwqNKTOG7ACZtR1xXXnzKln7EcFg"

genai.configure(api_key = apikey)
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

response = model.generate_content("Write a story about a magic backpack.")
print(response.text)