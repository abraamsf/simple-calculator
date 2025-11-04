from app.calculator import add, subtract, multiply, divide
import pytest # <-- Tambahkan ini

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 2) == 8

def test_divide():
    assert divide(6, 2) == 3

def test_divide_by_zero():
    # BARIS INI HARUS DIGANTI!
    with pytest.raises(ZeroDivisionError): # <-- Gunakan pytest.raises
        divide(5, 0)