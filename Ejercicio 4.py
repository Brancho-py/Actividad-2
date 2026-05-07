import math

class Circulo:
    def __init__(self, radio_cm):
        self.radio_cm = radio_cm
    
    def area(self):
        return math.pi * self.radio_cm ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio_cm


class Rectangulo:
    def __init__(self, base_cm, altura_cm):
        self.base_cm = base_cm
        self.altura_cm = altura_cm
    
    def area(self):
        return self.base_cm * self.altura_cm
    
    def perimetro(self):
        return 2 * (self.base_cm + self.altura_cm)


class Cuadrado:
    def __init__(self, lado_cm):
        self.lado_cm = lado_cm
    
    def area(self):
        return self.lado_cm ** 2
    
    def perimetro(self):
        return 4 * self.lado_cm


class TrianguloRectangulo:
    def __init__(self, base_cm, altura_cm):
        self.base_cm = base_cm
        self.altura_cm = altura_cm
    
    def hipotenusa(self):
        return math.sqrt(self.base_cm ** 2 + self.altura_cm ** 2)
    
    def area(self):
        return (self.base_cm * self.altura_cm) / 2
    
    def perimetro(self):
        return self.base_cm + self.altura_cm + self.hipotenusa()
    
    def tipo_triangulo(self):
        lado1 = self.base_cm
        lado2 = self.altura_cm
        lado3 = self.hipotenusa()
        
        if math.isclose(lado1, lado2) and math.isclose(lado2, lado3):
            return "Equilátero"
        elif math.isclose(lado1, lado2) or math.isclose(lado1, lado3) or math.isclose(lado2, lado3):
            return "Isósceles"
        else:
            return "Escaleno"


def mostrar_menu():
    print("\n--- MENÚ DE FIGURAS GEOMÉTRICAS ---")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Cuadrado")
    print("4. Triángulo Rectángulo")
    print("5. Salir")


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "5":
            print("Saliendo del programa...")
            break

        try:
            if opcion == "1":
                radio = float(input("Introduce el radio del círculo en cm: "))
                circulo = Circulo(radio)
                print("\nResultado Círculo:")
                print(f"  Área: {circulo.area():.2f} cm²")
                print(f"  Perímetro: {circulo.perimetro():.2f} cm")

            elif opcion == "2":
                base = float(input("Introduce la base del rectángulo en cm: "))
                altura = float(input("Introduce la altura del rectángulo en cm: "))
                rectangulo = Rectangulo(base, altura)
                print("\nResultado Rectángulo:")
                print(f"  Área: {rectangulo.area():.2f} cm²")
                print(f"  Perímetro: {rectangulo.perimetro():.2f} cm")

            elif opcion == "3":
                lado = float(input("Introduce el lado del cuadrado en cm: "))
                cuadrado = Cuadrado(lado)
                print("\nResultado Cuadrado:")
                print(f"  Área: {cuadrado.area():.2f} cm²")
                print(f"  Perímetro: {cuadrado.perimetro():.2f} cm")

            elif opcion == "4":
                base = float(input("Introduce la base (cateto horizontal) en cm: "))
                altura = float(input("Introduce la altura (cateto vertical) en cm: "))
                triangulo = TrianguloRectangulo(base, altura)
                print("\nResultado Triángulo Rectángulo:")
                print(f"  Hipotenusa: {triangulo.hipotenusa():.2f} cm")
                print(f"  Área: {triangulo.area():.2f} cm²")
                print(f"  Perímetro: {triangulo.perimetro():.2f} cm")
                print(f"  Tipo de triángulo: {triangulo.tipo_triangulo()}")

            else:
                print("Opción no válida. Por favor, selecciona un número del 1 al 5.")
        
        except ValueError:
            print("Error: Por favor, introduce únicamente valores numéricos (ej. 3.5).")
