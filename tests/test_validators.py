# tests/test_validators.py
from core.validators import PatternValidator

def test_email_valid():
    pv = PatternValidator()
    r = pv.validate_one("correo electrónico", "juan.perez@example.com")
    assert r.is_valid

def test_phone_invalid():
    pv = PatternValidator()
    r = pv.validate_one("teléfono", "abc123")
    assert not r.is_valid
