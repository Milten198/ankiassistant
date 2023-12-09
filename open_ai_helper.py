import requests
from langchain.chat_models import ChatOpenAI
import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'API key not found')

chain = ChatOpenAI(model="gpt-4-vision-preview", max_tokens=1024,
                   openai_api_key="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")

prompt = "Go through the text line by line and return only the words with the frame around them. " \
         "This frame looks like drawn by hand with a gray pencil. " \
         "There should be multiple words marked with such frame. " \
         "If you are not sure about any of the words return it anyway. " \
         "Ignore all the words with other color, font and size. " \
         "Return the list of words in format [word1, word2, word3]"


def extract_words_from_file(file):
    if OPENAI_API_KEY == 'API key not found':
        raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{prompt}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{file}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response
