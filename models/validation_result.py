# models/validation_result.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class ValidationResult:
    pattern_name: str
    text: str
    is_valid: bool
    start: Optional[int] = None
    end: Optional[int] = None
    message: Optional[str] = None
