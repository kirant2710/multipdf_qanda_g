import os
from typing import List
from PyPDF2 import PdfReader

class PdfProcessor:
    def load_pdfs(self, pdf_files: List[str]) -> List[str]:
        """Loads text from PDF files."""
        documents = []
        for pdf_file in pdf_files:
            with open(pdf_file, 'rb') as f:
                reader = PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                documents.append(text)
        return documents

    def preprocess_text(self, documents: List[str]) -> str:
        """Combines and preprocesses the text from the PDFs."""
        text = "\\n".join(documents)
        return text