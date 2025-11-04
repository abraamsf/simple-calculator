from app.calculator import add, subtract, multiply, divide
import pytest # Diperlukan untuk menggunakan pytest.raises

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 2) == 8

def test_divide():
    assert divide(6, 2) == 3

# --- Perbaikan di sini ---
def test_divide_by_zero():
    # Test ini akan berhasil jika memanggil divide(5, 0) menghasilkan ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
# -------------------------

