# app.py

import streamlit as st
from retrieve import retrieve_top_k
from generate import generate_answer

st.set_page_config(page_title="🤖 Personal Chatbot", layout="centered")
st.title("🤖 Ask Viswas — Your Personal AI Chatbot")

query = st.text_input("Ask a question about Viswas:")

if query:
    with st.spinner("Thinking..."):
        context = retrieve_top_k(query)
        answer = generate_answer(context, query)
        st.markdown("### 📌 Answer:")
        st.write(answer)
        
