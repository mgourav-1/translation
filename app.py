import streamlit as st
import os
import google.generativeai as genai

# Set up the model
generation_config = {
    "temperature": 0,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

# Set Google API key
genai.configure(api_key='AIzaSyBBudklTljBGm2xx8F1iiDzqUHB7epKALk')
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Define Streamlit UI
st.title("Translation ChatBot")

# Prompt the user to paste their code
user_input = st.text_area("Please enter the text to be translated here:")

translateTo = st.selectbox(
    'Translate the text in?',
    ('Hindi', 'Spanish', 'German', 'Japanese', 'Chinese', 'Arabic', 'English'))

tone = st.selectbox(
    'Select the tone',
    ('Angry', 'Happy', 'Sad', 'Excited'))

if st.button("Translate"):
    # Check if the user input is empty or contains only whitespace
    if user_input.strip() == "":
        st.error("Input is out of context. Please provide  valid text.")
    else:
        prompt_parts = ["""Translate """ + user_input + """ which is in English to """ + translateTo + """ with """ + tone + """ tone"""]

        response = model.generate_content(prompt_parts)
        st.markdown(response.text)
