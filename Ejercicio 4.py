import math

class Circulo:
    #Representa un círculo con un radio dado.
    
    def __init__(self, radio_cm):
        self.radio_cm = radio_cm
    
    def area(self):
        #Calcula el área del círculo: π * r².
        return math.pi * self.radio_cm ** 2
    
    def perimetro(self):
        #Calcula el perímetro (circunferencia): 2 * π * r.
        return 2 * math.pi * self.radio_cm

class Rectangulo:
    #Representa un rectángulo con base y altura.
    
    def __init__(self, base_cm, altura_cm):
        self.base_cm = base_cm
        self.altura_cm = altura_cm
    
    def area(self):
        #Área del rectángulo: base * altura.
        return self.base_cm * self.altura_cm
    
    def perimetro(self):
        #Perímetro del rectángulo: 2 * (base + altura).
        return 2 * (self.base_cm + self.altura_cm)

class Cuadrado:
    #Representa un cuadrado (lado igual).
    
    def __init__(self, lado_cm):
        self.lado_cm = lado_cm
    
    def area(self):
        #Área del cuadrado: lado².
        return self.lado_cm ** 2
    
    def perimetro(self):
        #Perímetro del cuadrado: 4 * lado.
        return 4 * self.lado_cm

class TrianguloRectangulo:
    #Representa un triángulo rectángulo con base y altura como catetos.
    
    def __init__(self, base_cm, altura_cm):
        self.base_cm = base_cm      # cateto horizontal
        self.altura_cm = altura_cm   # cateto vertical
    
    def hipotenusa(self):
        #Calcula la hipotenusa usando el teorema de Pitágoras.
        return math.sqrt(self.base_cm ** 2 + self.altura_cm ** 2)
    
    def area(self):
        #Área del triángulo rectángulo: (base * altura) / 2.
        return (self.base_cm * self.altura_cm) / 2
    
    def perimetro(self):
        #Perímetro: suma de los tres lados (base + altura + hipotenusa).
        return self.base_cm + self.altura_cm + self.hipotenusa()
    
    def tipo_triangulo(self):
        """
        Determina el tipo de triángulo según la longitud de sus lados.
        Lados: cateto1 (base), cateto2 (altura), hipotenusa.
        Retorna: 'Equilátero', 'Isósceles' o 'Escaleno'.
        """
        lado1 = self.base_cm
        lado2 = self.altura_cm
        lado3 = self.hipotenusa()
        
        # Comparamos con tolerancia por si hay errores de precisión
        if math.isclose(lado1, lado2) and math.isclose(lado2, lado3):
            return "Equilátero"
        elif math.isclose(lado1, lado2) or math.isclose(lado1, lado3) or math.isclose(lado2, lado3):
            return "Isósceles"
        else:
            return "Escaleno"

if __name__ == "__main__":
    # Crear instancias de cada figura con valores de ejemplo
    circulo = Circulo(radio_cm=5)
    rectangulo = Rectangulo(base_cm=4, altura_cm=6)
    cuadrado = Cuadrado(lado_cm=3)
    triangulo = TrianguloRectangulo(base_cm=3, altura_cm=4)

    # Probar métodos del círculo
    print("Círculo:")
    print(f"  Radio: {circulo.radio_cm} cm")
    print(f"  Área: {circulo.area():.2f} cm²")
    print(f"  Perímetro: {circulo.perimetro():.2f} cm")
    print()

    # Probar métodos del rectángulo
    print("Rectángulo:")
    print(f"  Base: {rectangulo.base_cm} cm, Altura: {rectangulo.altura_cm} cm")
    print(f"  Área: {rectangulo.area()} cm²")
    print(f"  Perímetro: {rectangulo.perimetro()} cm")
    print()

    # Probar métodos del cuadrado
    print("Cuadrado:")
    print(f"  Lado: {cuadrado.lado_cm} cm")
    print(f"  Área: {cuadrado.area()} cm²")
    print(f"  Perímetro: {cuadrado.perimetro()} cm")
    print()

    # Probar métodos del triángulo rectángulo
    print("Triángulo rectángulo:")
    print(f"  Base: {triangulo.base_cm} cm, Altura: {triangulo.altura_cm} cm")
    print(f"  Hipotenusa: {triangulo.hipotenusa():.2f} cm")
    print(f"  Área: {triangulo.area():.2f} cm²")
    print(f"  Perímetro: {triangulo.perimetro():.2f} cm")
    print(f"  Tipo de triángulo: {triangulo.tipo_triangulo()}")