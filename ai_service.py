import streamlit as st
import json
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

import google.generativeai as genai # import Gemini API library

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-lite", #can also change model according to need
    generation_config={
        "temperature": 0.3,
        "max_output_tokens": 1500,
        "top_p": 1,
    }
)

#to avoid Api calls on every interaction
@st.cache_data

# Function to fetch questions from OpenAI API
def fetch_questions(text_content, quiz_level):

    RESPONSE_JSON = {
        "mcqs" : [
            {
                "mcq" : "multiple choice question 1",
                "options" : {
                    "a" : "choice here1",
                    "b" : "choice here2",
                    "c" : "choice here3",
                    "d" : "choice here4",
                },
                "correct": "a",
            }          
        ]
    }

    # prompt template for generating MCQs 
    PROMPT_TEMPLATE = """
    Text: {text_content}

    You are an expert MCQ generator.

    Generate exactly 5 MCQs at {quiz_level} level.

    Return ONLY valid JSON.
    Do NOT add explanations.
    Do NOT add markdown.
    Do NOT add extra text.

    The response MUST strictly follow this JSON format:

    {RESPONSE_JSON}
    """
   
    formatted_template = PROMPT_TEMPLATE.format(text_content=text_content, quiz_level=quiz_level,RESPONSE_JSON=json.dumps(RESPONSE_JSON, indent=2))
    
    #Make API request to OpenAI (get for openai documentation)
    response = model.generate_content(formatted_template)
    

    #Extract content from response
    extracted_response = response.text.strip()

    # Remove markdown if present
    extracted_response = extracted_response.replace("```json", "").replace("```", "")

    print(extracted_response)

    try:                                                #to handle json decode error
        parsed = json.loads(extracted_response)
        return parsed.get("mcqs", [])
    except json.JSONDecodeError:
        st.error(" AI returned invalid JSON.")
        st.code(extracted_response)  # show raw response for debugging
        return []
