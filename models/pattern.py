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
            # Acepta únicamente números móviles colombianos de 10 dígitos que comienzan por 3,
            # en dos formatos permitidos: "3104561168" o "310 456 1168".
            # No acepta +57, guiones, ni otros formatos.
            regex=r"(?<!\d)(?:3\d{9}|3\d{2}\s\d{3}\s\d{4})(?!\d)",
            description="Teléfono móvil colombiano: 10 dígitos, empieza por 3. Formatos: 3104561168 o 310 456 1168"
        )

    def example(self):
        return "3104561168 sin el +57"




class DatePattern(Pattern):
    def __init__(self):
        super().__init__(
            name="Fecha",
            regex=r"\b(?:(?:[0-3]?\d[\/\-](?:0?[1-9]|1[0-2])[\/\-](?:\d{2}|\d{4}))|(?:\d{4}[\/\-](?:0?[1-9]|1[0-2])[\/\-][0-3]?\d))\b",
            description="Detecta fechas en formato DD/MM/YYYY o YYYY-MM-DD."
        )

    def example(self):
        return "2024-05-21 o 12/04/2023"


class URLPattern(Pattern):
    def __init__(self):
        super().__init__(
            name="URL",
            regex=r"\b(?:https?://)?(?:www\.)?[A-Za-z0-9\-]+\.[A-Za-z]{2,}(?:[/?#][^\s]*)?\b",
            description="Valida direcciones web con o sin prefijo http/https."
        )

    def example(self):
        return "https://www.ejemplo.com"
    

# Demás patrones que faltaban

class CedulaPattern(Pattern):
    def __init__(self):
        super().__init__(
            name="Cédula",
            regex=r"\b\d{6,10}\b",
            description="Detecta cédulas colombianas (6-10 dígitos)."
        )

    def example(self):
        return "1025487963"


class PlacaPattern(Pattern):
    def __init__(self):
        super().__init__(
            name="Placa vehicular",
            regex=r"(?i)(?<!\S)(?:[A-Z]{3}\d{3}|[A-Z]{3}\d{2}[A-Z]?)(?!\S)",
            description="Placas Colombia carros (ABC123) y motos (ABC12 o ABC12D), sin guiones, mayúsculas o minúsculas."
        )

    def example(self):
        return "ABC123 (Carro) ABC12 O ABC12D (Moto)"


class PostalCodePattern(Pattern):
    def __init__(self):
        super().__init__(
            name="Código Postal",
            regex=r"(?<!\d)(?:\d{6}|\d{5}(?:-\d{4})?)(?!\d)",
            description="Código postal colombiano (6 dígitos) o internacional (5 dígitos) y ZIP+4 opcional."
        )

    def example(self):
        return "630004"


class StrongPasswordPattern(Pattern):
    def __init__(self):
        super().__init__(
            name="Contraseña Segura",
            regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&._-])[A-Za-z\d@$!%*?&._-]{8,}$",
            description="Debe tener al menos 8 caracteres, mayúscula, minúscula, número y símbolo."
        )

    def example(self):
        return "Segura@123"

