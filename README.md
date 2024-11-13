# Document Translator

This project provides a Python-based solution for translating PDF documents. It extracts text from an input PDF, translates the text using Google Cloud Translation, and outputs the translated content in a new PDF file. The project is generalized for any language translation supported by Google Cloud Translation and can handle documents in various languages.

## Features

- **Text Extraction from PDF**: Extracts all text from each page of a PDF document.
- **Translation Using Google Cloud Translation API**: Translates the extracted text to the specified target language.
- **PDF Creation**: Saves the translated text as a new PDF document.
- **Logging**: Logs key steps, including partial text extracted and translated, for easier debugging.

## Prerequisites

To run this project, you will need:

1. **Python 3.x**
2. **Google Cloud Translation API Key**: Set up an API key and download the credentials file (JSON format) from Google Cloud.
3. **Python Packages**: Install the following packages:
   ```sh
   pip install fpdf PyPDF2 google-cloud-translate
