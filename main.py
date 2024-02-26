import json
import logging
from datetime import datetime
import argparse
from converters import PdfToText, JPGToText, PdfToJPG
from ia import GeminiApi, OpenIAApi

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file_path", help="Passe o caminho do arquivo pdf")
parser.add_argument("-t", "--file_type", help="Passe o tipo de arquivo: pdf_image, pdf_text, image ou text.")


class Extractor:
    def execute(self, path_pdf: str, type: str) -> None:
        match type:
            case "pdf_image":
                extract = ""
                images = PdfToJPG(path_pdf)
                logging.warning('Extraction started with tesseract...')
                for image in images.result[0]['output_jpgfiles']:
                    text = JPGToText(image)
                    extract += text.result
                logging.warning('Extraction finished.')
                return extract
            
            case "pdf_text":
                extract = PdfToText(path_pdf)
                return extract
            
            case "image":
                extract = JPGToText(path_pdf)
                return extract
            
            case "text":
                with open(path_pdf, 'r') as file_txt:
                    extract = file_txt.read()
                    return extract

if __name__ == '__main__':
    args = parser.parse_args()
    file_path = args.file_path
    file_type = args.file_type
    extractor = Extractor()
    match file_type:
        case "pdf_image":
            text = extractor.execute(file_path, file_type)
            ia = GeminiApi()
            response = ia.to_ask(text)
            file_name = f"{file_path}_{datetime.now()}.json"
            logging.warning(f'the file: {file_name} is ready! \n')
            with open(file_name, "w") as file:
               file.write(response)
    
        case "pdf_text":
            text = extractor.execute(file_path, file_type)
            ia = GeminiApi()
            response = ia.to_ask(text)
            print(response.text)

        case "image":
            text = extractor.execute(file_path, file_type)
            ia = GeminiApi()
            response = ia.to_ask(text)
            print(response.text)

        case "text":
            text = extractor.execute(file_path, file_type)
            ia = GeminiApi()
            response = ia.to_ask(text)
            print(response.text)

        case "":
            logging.warning("file type is required")
    
