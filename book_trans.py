import os

from PyPDF2 import PdfFileReader
#from googletrans import Translator
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate

from translate_pdfs.fonts import *

from deep_translator import GoogleTranslator
# translated = GoogleTranslator(source='auto', target='ru').translate("keep it up, you are awesome")

from deep_translator import GoogleTranslator

"""
This script uses Google Translate library to translate the PDF
"""

"""
Constants
"""
URL_COM = 'translate.googleapis.com'
LANG = "ru"

"""
FUNCTIONS
"""
# path = "book.pdf"
# translated = MyMemoryTranslator(source='en', target='ru').translate_file(path)

def get_translated_page_content(reader, lang):
    """
    Reads page content from the reader, translates it,
    cleans it and returns page content as a list of strings.
    Each entry in list represents a page
    """
    num_pages = reader.numPages
    page_contents = []
    # translator = Translator(service_urls=[URL_COM])
    # translated = MyMemoryTranslator(source='en', target='ru').translate_file(path)
    # translated = GoogleTranslator(source='auto', target='ru').translate_file(path)
    for p in range(num_pages):
        page = reader.getPage(p)
        text = page.extractText()
        # translation = translator.translate(text, dest=lang)
        # translation = MyMemoryTranslator(source='en', target='ru').translate(text)
        translation = GoogleTranslator(source='en', target='ru').translate(text)
        result_text = translation.text.replace("\n", " ").replace("W", "")
        page_contents.append(result_text)
    return page_contents


def translate_pdf(path, lang):
    file = open(path, 'rb')
    reader = PdfFileReader(file)
    page_contents = get_translated_page_content(reader, lang)

    page_text = []
    name = f'{LANG}_{path}'
    pdf = SimpleDocTemplate(name, pagesize=letter)

    for text in page_contents:
        page_text.append(
            Paragraph(text, encoding='utf-8', style=regular))

    pdf.build(page_text)


if __name__ == '__main__':
    file_name = "book.pdf"
    translate_pdf(file_name, LANG)
