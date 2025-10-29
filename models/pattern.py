# models/pattern.py
import re
from abc import ABC, abstractmethod

class Pattern(ABC):
    """Clase abstracta base para definir patrones con regex y métodos de validación."""

    def __init__(self, name: str, regex: str, description: str):
        self.name = name
        self.regex = re.compile(regex, re.IGNORECASE)
        self.description = description

    def find_all(self, text: str):
        """Devuelve todas las coincidencias del patrón en un texto."""
        return [(m.start(), m.end(), m.group()) for m in self.regex.finditer(text)]

    def validate(self, text: str) -> bool:
        """Valida si un texto completo cumple con el patrón."""
        return bool(self.regex.fullmatch(text.strip()))

    @abstractmethod
    def example(self) -> str:
        """Debe devolver un ejemplo válido del patrón."""
        pass


# 🔸 Subclases específicas para cada tipo de patrón

class EmailPattern(Pattern):
    def __init__(self):
        super().__init__(
            name="Correo electrónico",
            regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
            description="Valida direcciones de correo electrónico."
        )

    def example(self):
        return "usuario@dominio.com"


class PhonePattern(Pattern):
    def __init__(self):
        super().__init__(
            name="Teléfono",
            regex=r"\b(?:\+?\d{1,3}[\s-]?)?(?:\(?\d{1,4}\)?[\s-]?)?\d{4,14}\b",
            description="Detecta números telefónicos locales o internacionales."
        )

    def example(self):
        return "+57 300 123 4567"


class DatePattern(Pattern):
    def __init__(self):
        super().__init__(
            name="Fecha",
            regex=r"\b(?:(?:[0-3]?\d[\/\-](?:0?[1-9]|1[0-2])[\/\-](?:\d{2}|\d{4}))|(?:\d{4}[\/\-](?:0?[1-9]|1[0-2])[\/\-][0-3]?\d))\b",
            description="Detecta fechas en formato DD/MM/YYYY o YYYY-MM-DD."
        )

    def example(self):
        return "2024-05-21"


class URLPattern(Pattern):
    def __init__(self):
        super().__init__(
            name="URL",
            regex=r"\b(?:https?://)?(?:www\.)?[A-Za-z0-9\-]+\.[A-Za-z]{2,}(?:[/?#][^\s]*)?\b",
            description="Valida direcciones web con o sin prefijo http/https."
        )

    def example(self):
        return "https://www.ejemplo.com"
