"""
Módulo de operaciones básicas y cálculo de promedios.
Incluye clases para realizar operaciones matemáticas simples.
"""

class OperacionesBasicas:
    """Clase que realiza operaciones básicas como suma y resta."""

    def __init__(self):
        """Inicializa la clase con un resultado en 0."""
        self.resultado = 0

    def sumar(self, a, b):
        """Esta función suma dos números y almacena el resultado."""
        self.resultado = a + b

    def restar(self, a, b):
        """Esta función resta dos números y almacena el resultado."""
        self.resultado = a - b

    def obtener_resultado(self):
        """Devuelve el resultado actual de la operación realizada."""
        return self.resultado


class CalculadoraPromedio:
    """Clase que calcula el promedio de una lista de valores."""

    def __init__(self, valores):
        """Inicializa la clase con una lista de valores."""
        self.valores = valores

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de la lista de valores proporcionada."""
        suma = 0
        for valor in self.valores:
            suma += valor
        resultado_promedio = suma / len(self.valores)  # Cambio de nombre para evitar conflictos
        return resultado_promedio

    def obtener_valores(self):
        """Devuelve la lista de valores almacenados en la clase."""
        return self.valores


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio_resultado = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedio_resultado}")
