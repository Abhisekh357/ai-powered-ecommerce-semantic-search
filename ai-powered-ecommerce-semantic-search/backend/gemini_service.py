import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("Gemini API Key not found!")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(query, retrieved_products):

    context = ""

    for product in retrieved_products:
        context += (
            f"Product: {product['name']}\n"
            f"Description: {product['description']}\n\n"
        )

    prompt = f"""
You are an AI shopping assistant.

Use ONLY the products below.

Products:

{context}

User Query:
{query}

Recommend the most relevant products and explain why.
"""

    response = model.generate_content(prompt)

    return response.text