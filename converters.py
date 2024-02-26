import pytesseract
import PyPDF2
from typing import Protocol
from pdf2jpg import pdf2jpg
from PIL import Image

class PdfExtract(Protocol):
    def result(self) -> None:...

class PdfToText(PdfExtract):
    def __init__(self, pdf: str):
        self.__pdf = pdf

    @property
    def result(self):
        text = ""
        
        with open(self.__pdf, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text
    
class PdfToJPG(PdfExtract):
    def __init__(self, pdf: str) -> None:
        self.__pdf = pdf

    @property
    def result(self):
        return pdf2jpg.convert_pdf2jpg(self.__pdf, 'imagens/', dpi=300, pages="ALL")

class JPGToText(PdfExtract):
    def __init__(self, jpg: str) -> None:
        self.__jpg = jpg

    @property
    def result(self):
        return pytesseract.image_to_string(Image.open(self.__jpg))