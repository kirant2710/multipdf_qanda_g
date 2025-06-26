import google.generativeai as genai

class GeminiApi:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def ask_question(self, context: str, question: str) -> str:
        """Asks a question to the Gemini API using the provided context."""
        prompt = f"""Answer the question based on the context below.
        Context: {context}
        Question: {question}"""
        response = self.model.generate_content(prompt)
        return response.text