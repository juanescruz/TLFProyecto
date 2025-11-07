# models/validation_result.py
from dataclasses import dataclass
from typing import Optional

"""
Representa el resultado de validar o detectar un patrón,
almacenando el texto encontrado y su estado (válido o no).
"""

@dataclass
class ValidationResult:
    pattern_name: str
    text: str
    is_valid: bool
    start: Optional[int] = None
    end: Optional[int] = None
    message: Optional[str] = None
