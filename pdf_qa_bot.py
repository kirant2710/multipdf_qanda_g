import os
from dotenv import load_dotenv
from pdf_processor import PdfProcessor
from gemini_api import GeminiApi

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("No Gemini API key found in .env file")

    pdf_processor = PdfProcessor()
    gemini_api = GeminiApi(api_key)

    pdf_folder = "pdfs"
    pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

    if not pdf_files:
        raise ValueError("No PDF files found in the 'pdfs' folder")

    documents = pdf_processor.load_pdfs(pdf_files)
    text = pdf_processor.preprocess_text(documents)

    while True:
        question = input("Ask a question (or type 'exit' to quit): ")
        if question.lower() == "exit":
            break

        answer = gemini_api.ask_question(text, question)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()