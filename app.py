import streamlit as st
from utils import get_chain

st.set_page_config(page_icon='📚',
                   page_title="Chat💬 with Database📚",                  
)

st.title("Chat💬 with Database📚")

question = st.text_area("Question: ")

if st.button('Get Answer'):
    if question:
        response = get_chain(question)
        st.header("Answer")
        st.write(response)