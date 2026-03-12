from pathlib import Path

import pytesseract
from PIL import Image
from pypdf import PdfReader


class FileProcessingService:
    @staticmethod
    def extract_pdf_text(path: str) -> str:
        reader = PdfReader(path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    @staticmethod
    def extract_image_text(path: str) -> str:
        image = Image.open(path)
        return pytesseract.image_to_string(image)

    @staticmethod
    def ensure_storage_dir(base_path: str) -> Path:
        path = Path(base_path)
        path.mkdir(parents=True, exist_ok=True)
        return path
