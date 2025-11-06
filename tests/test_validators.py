# tests/test_validators.py
from core.validators import PatternValidator

#Test Email
def test_email_valid():
    pv = PatternValidator()
    r = pv.validate_one("correo electrónico", "juan.perez@example.com")
    assert r.is_valid

#Test Cedula
def test_cedula_valid():
    pv = PatternValidator()
    r = pv.validate_one("cédula", "1025487963")
    assert r.is_valid

#Test Contraseña
def test_password_secure():
    pv = PatternValidator()
    r = pv.validate_one("contraseña segura", "Abcde@123")
    assert r.is_valid

def test_password_weak():
    pv = PatternValidator()
    r = pv.validate_one("contraseña segura", "abc123")
    assert not r.is_valid

#Test Teléfonos
def test_phone_valid_plain():
    pv = PatternValidator()
    r = pv.validate_one("teléfono", "3104561168")
    assert r.is_valid

def test_phone_valid_spaced():
    pv = PatternValidator()
    r = pv.validate_one("teléfono", "310 456 1168")
    assert r.is_valid

def test_phone_invalid_plus57():
    pv = PatternValidator()
    r = pv.validate_one("teléfono", "+57 3104561168")
    assert not r.is_valid

def test_phone_not_cedula_or_postal():
    pv = PatternValidator()
    # cédula de 10 dígitos no debe pasar como teléfono (según orden + patrones específicos)
    r_ced = pv.validate_one("cédula", "1025487963")
    assert r_ced.is_valid
    # validar que el mismo número no sea considerado teléfono
    r_phone = pv.validate_one("teléfono", "1025487963")
    assert not r_phone.is_valid

#Test placas vehiculares
def test_car_plate_valid():
    pv = PatternValidator()
    r = pv.validate_one("placa vehicular", "ABC123")
    assert r.is_valid

def test_motorcycle_plate_valid_2digits():
    pv = PatternValidator()
    r = pv.validate_one("placa vehicular", "NRJ95")
    assert r.is_valid

def test_motorcycle_plate_valid_2digits_letter():
    pv = PatternValidator()
    r = pv.validate_one("placa vehicular", "NRJ95E")
    assert r.is_valid

def test_plate_lowercase():
    pv = PatternValidator()
    r = pv.validate_one("placa vehicular", "abc123")
    assert r.is_valid

def test_plate_invalid_dash():
    pv = PatternValidator()
    r = pv.validate_one("placa vehicular", "ABC-123")
    assert not r.is_valid

def test_plate_invalid_length():
    pv = PatternValidator()
    r = pv.validate_one("placa vehicular", "AB123")
    assert not r.is_valid

#Test Codigos Postales
def test_postal_colombia_6_digits():
    pv = PatternValidator()
    r = pv.validate_one("código postal", "630004")
    assert r.is_valid

def test_postal_colombia_5_digits():
    pv = PatternValidator()
    r = pv.validate_one("código postal", "05001")
    assert r.is_valid

def test_postal_zip_plus_4():
    pv = PatternValidator()
    r = pv.validate_one("código postal", "05001-1234")
    assert r.is_valid

def test_postal_invalid_letters():
    pv = PatternValidator()
    r = pv.validate_one("código postal", "63A004")
    assert not r.is_valid

def test_postal_invalid_length():
    pv = PatternValidator()
    r = pv.validate_one("código postal", "63000")
    assert not r.is_valid


