# core/extractor.py
from core.validators import PatternValidator
import pandas as pd

class PatternExtractor:
    """Motor de extracción masiva de patrones."""

    def __init__(self):
        self.validator = PatternValidator()

    def extract_from_text(self, text: str):
        results = self.validator.validate_all(text)
        return pd.DataFrame([r.__dict__ for r in results])

    def extract_from_file(self, filepath: str):
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        return self.extract_from_text(text)
