import logging
from fpdf import FPDF
import PyPDF2
import logging
import os
from google.cloud import translate_v2 as translate

# Set environment variables
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/mnt/c/Users/Nikita/Music/translator/translatevn-422707-b030db79fb0b.json'

def translate_text_google(text, target_language='en'):
    client = translate.Client()
    try:
        # Translate the text
        result = client.translate(text, target_language=target_language)
        # Access the translated text using the key 'translatedText'
        return result['translatedText']
    except KeyError as e:
        print(f"Key error: {e}")
        return text
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return text


def translate_text(text, dest_language='en'):
    paragraphs = text.split('\n\n')
    translated_paragraphs = []

    for paragraph in paragraphs:
        if paragraph.strip():
            if paragraph == "":
                pass
            else:
                translated_paragraph = translate_text_google(paragraph, target_language=dest_language)
                translated_paragraphs.append(translated_paragraph)
    return '\n\n'.join(translated_paragraphs)


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
    return "\n".join(text)



def translate_pdf_file(input_pdf, output_pdf, target_language='en'):
    extracted_text = extract_text_from_pdf(input_pdf)
    logging.debug(f"Extracted text: {extracted_text[:500]}")  # Log first 500 characters to check
    translated_text = translate_text(extracted_text, dest_language=target_language)
    logging.debug(f"Translated text: {translated_text[:500]}")  # Log first 500 characters to check
    create_pdf_from_text(translated_text, output_pdf)

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        # Update the path to where you've stored DejaVuSansCondensed.ttf
        font_path = 'fonts/Noto_Sans/NotoSans-VariableFont.ttf'
        self.add_font('Noto_Sans', '', font_path)
        self.set_font('Noto_Sans', '', 14)  # Using 14 as the font size

def create_pdf_from_text(text, output_filename):
    pdf = PDF()
    pdf.add_page()
    pdf.multi_cell(0, 10, text)
    pdf.output(output_filename)

# Example usage
inp_path = input("Enter the path to your pdf file: ")
translate_pdf_file(inp_path, "jap-en.pdf")
