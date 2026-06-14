# test_calculadora.py

from calculadora import suma, resta, multiplicacion, division

def test_suma():
    """Prueba la función suma"""
    assert suma(5, 3) == 8
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(100, 200) == 300

def test_resta():
    """Prueba la función resta"""
    assert resta(10, 4) == 6
    assert resta(0, 5) == -5
    assert resta(100, 50) == 50
    assert resta(5, 10) == -5

def test_multiplicacion():
    """Prueba la función multiplicacion"""
    assert multiplicacion(3, 4) == 12
    assert multiplicacion(0, 5) == 0
    assert multiplicacion(-2, 3) == -6
    assert multiplicacion(7, 7) == 49

def test_division():
    """Prueba la función division"""
    assert division(10, 2) == 5
    assert division(9, 3) == 3
    assert division(100, 4) == 25
    assert division(7, 2) == 3.5

def test_division_por_cero():
    """Prueba que division por cero lanza excepción"""
    try:
        division(10, 0)
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass  # Esto es correcto, la excepción se lanzó