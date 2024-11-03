import os
import re
import google.generativeai as genai

class consultantAI:
    def __init__(self):
        api_key = os.environ.get('GOOGLE_API_KEY')
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def read_report(self, file_path):
        """Read and return the content of a file."""
        with open(file_path, 'r') as file:
            return file.read()

    def remove_markdown(self, text):
        """Remove common markdown formatting from text."""
        # Remove headers
        text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
        # Remove bold/italic
        text = re.sub(r'\*{1,3}', '', text)
        # Remove inline code
        text = re.sub(r'`', '', text)
        # Remove links
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        # Remove bullet points
        text = re.sub(r'^\s*[-*+]\s*', '', text, flags=re.MULTILINE)
        return text.strip()

    def generate_solution(self, prompt, system_message=None):
        """Generate a solution using Google's Generative AI based on the given prompt."""
        if system_message is None:
            system_message = "You're a web security consultant. Give solutions and feedback in a minimized and organized way. Always use icons."

        full_prompt = f"{system_message}\n\nUser: {prompt}"

        try:
            response = self.model.generate_content(full_prompt)
            return self.remove_markdown(response.text)
        except genai.types.generation_types.BlockedPromptException:
            print("The prompt was blocked due to safety concerns.")
        except genai.types.generation_types.GenerationException as e:
            print(f"Generation failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return None
