# calculadora.py

def suma(a, b):
    """Devuelve la suma de a y b"""
    return a + b

def resta(a, b):
    """Devuelve la resta de a y b"""
    return a - b

def multiplicacion(a, b):
    """Devuelve la multiplicación de a y b"""
    return a * b

def division(a, b):
    """Devuelve la división de a entre b"""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

# Pruebas simples al ejecutar el archivo directamente
if __name__ == "__main__":
    print("=== CALCULADORA ===")
    print(f"Suma: 5 + 3 = {suma(5, 3)}")
    print(f"Resta: 5 - 3 = {resta(5, 3)}")
    print(f"Multiplicación: 5 * 3 = {multiplicacion(5, 3)}")
    print(f"División: 6 / 3 = {division(6, 3)}")
    print("==================")


def potencia(a, b):
    return a ** b
print(f"Potencia: 2^3 = {potencia(2, 3)}")
