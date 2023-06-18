# Integrate code
import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st

os.environ['OPENAI_API_KEY'] =openai_key

# Streamlit framework

st.title('Welcome To Langchian With OpenAI API')
input_text=st.text_input('Search for your interested topic')

# OpenAI LLMS
llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
