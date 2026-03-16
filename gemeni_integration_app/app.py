from google import genai
import os
from dotenv import load_dotenv


load_dotenv(override=True)

client = genai.Client(api_key=os.getenv("API_KEY"))

print("You are now chatting with Gemini, model 2.5 flash. To exit chat mode simply type 'q'.")
while True:
    user_input = input('You: ')

    if user_input.lower() == 'q':
        print('Chat session ended!')
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    print('Gemini: ', response.text)
