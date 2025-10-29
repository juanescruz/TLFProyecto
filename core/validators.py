# core/validators.py
from models.pattern import EmailPattern, PhonePattern, DatePattern, URLPattern
from models.validation_result import ValidationResult

class PatternValidator:
    """Gestor de validaciones: centraliza la ejecución de patrones."""

    def __init__(self):
        self.patterns = [
            EmailPattern(),
            PhonePattern(),
            DatePattern(),
            URLPattern()
        ]

    def validate_all(self, text: str):
        """Valida y extrae todos los patrones en un texto."""
        results = []
        for p in self.patterns:
            matches = p.find_all(text)
            for (start, end, match) in matches:
                results.append(
                    ValidationResult(
                        pattern_name=p.name,
                        text=match,
                        is_valid=p.validate(match),
                        start=start,
                        end=end,
                        message="Coincidencia encontrada"
                    )
                )
        return results

    def validate_one(self, pattern_name: str, text: str):
        """Valida un único campo según el patrón elegido."""
        for p in self.patterns:
            if p.name.lower() == pattern_name.lower():
                valid = p.validate(text)
                return ValidationResult(
                    pattern_name=p.name,
                    text=text,
                    is_valid=valid,
                    message="Válido ✅" if valid else f"Inválido ❌ — Ejemplo: {p.example()}"
                )
        raise ValueError(f"Patrón '{pattern_name}' no encontrado.")
