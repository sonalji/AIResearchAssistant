import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key is None:
    raise ValueError("GROQ_API_KEY not found in .env")

client = Groq(api_key=api_key)

def build_context(retrieved_chunks):

    context = []

    for result in retrieved_chunks:

        metadata = result["metadata"]

        page = metadata["page"]

        text = metadata["text"]

        context.append(
            f"[Page {page}]\n{text}"
        )

    return "\n\n".join(context)

def generate_research_response(user_query, retrieved_chunks):

    context = build_context(retrieved_chunks)

    system_prompt = """
You are an EEG AI Research Assistant.

Answer ONLY from the supplied context.

If the answer cannot be found, respond exactly:

Information not found in database.

Always mention the page number(s) used.
"""

    user_prompt = f"""
Context

{context}

Question

{user_query}
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        temperature=0,

        messages=[

            {
                "role": "system",
                "content": system_prompt
            },

            {
                "role": "user",
                "content": user_prompt
            }

        ]
    )

    return response.choices[0].message.content