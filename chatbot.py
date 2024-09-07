import streamlit as st
import google.generativeai as genai
st.set_page_config(
    page_title = 'Chatbot',
    page_icon = '?',
    layout = 'centered',
)

st.header("🤖 Get Answers")
question = st.text_input("Ask Me questions that are appropriate (so you dont break me lol)")
genai.configure(api_key = 'AIzaSyBHCCtq4qtkzRuyjZaKJL9UT_5_G3c3rDU')
model = genai.GenerativeModel("gemini-1.5-flash")
if question:
    response = model.generate_content(question, generation_config= genai.types.GenerationConfig(
        candidate_count= 1,
        max_output_tokens = 1000,
        temperature= 1.5,
    ),)
    st.write(response.text)
