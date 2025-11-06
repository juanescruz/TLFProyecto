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

def test_cedula_valid():
    pv = PatternValidator()
    r = pv.validate_one("cédula", "1025487963")
    assert r.is_valid

def test_placa_valid():
    pv = PatternValidator()
    r = pv.validate_one("placa vehicular", "ABC-123")
    assert r.is_valid

def test_postal_invalid():
    pv = PatternValidator()
    r = pv.validate_one("código postal", "ABCDE")
    assert not r.is_valid

def test_password_secure():
    pv = PatternValidator()
    r = pv.validate_one("contraseña segura", "Abcde@123")
    assert r.is_valid

def test_password_weak():
    pv = PatternValidator()
    r = pv.validate_one("contraseña segura", "abc123")
    assert not r.is_valid

