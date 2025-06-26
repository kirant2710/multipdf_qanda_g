import streamlit as st
import os
from dotenv import load_dotenv
from pdf_processor import PdfProcessor
from gemini_api import GeminiApi

def main():
    st.title("PDF Question Answering Bot")

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("No Gemini API key found in .env file")
        return

    pdf_processor = PdfProcessor()
    gemini_api = GeminiApi(api_key)

    pdf_folder = "pdfs"
    pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

    if not pdf_files:
        st.error("No PDF files found in the 'pdfs' folder")
        return

    documents = pdf_processor.load_pdfs(pdf_files)
    text = pdf_processor.preprocess_text(documents)

    question = st.text_input("Ask a question:")
    if question:
        answer = gemini_api.ask_question(text, question)
        st.write("Answer:", answer)

if __name__ == "__main__":
    main()