from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"


class Planeta:
    def __init__(self, nombre=None, cantidad_satelites=0, masa_kg=0.0, volumen_km3=0.0,
                 diametro_km=0, distancia_media_sol_millones_km=0,
                 tipo_planeta=TipoPlaneta.TERRESTRE, observable=False):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa_kg = masa_kg
        self.volumen_km3 = volumen_km3
        self.diametro_km = diametro_km
        self.distancia_media_sol_millones_km = distancia_media_sol_millones_km
        self.tipo_planeta = tipo_planeta
        self.observable = observable

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa (kg): {self.masa_kg}")
        print(f"Volumen (km³): {self.volumen_km3}")
        print(f"Diámetro (km): {self.diametro_km}")
        print(f"Distancia media al Sol (millones km): {self.distancia_media_sol_millones_km}")
        print(f"Tipo de planeta: {self.tipo_planeta.value}")
        print(f"Observable a simple vista: {'Sí' if self.observable else 'No'}")

    def calcular_densidad(self):
        if self.volumen_km3 == 0:
            return float('inf')
        return self.masa_kg / self.volumen_km3

    def es_exterior(self):
        distancia_km = self.distancia_media_sol_millones_km * 1e6
        UA_en_km = 149597870
        distancia_ua = distancia_km / UA_en_km
        return distancia_ua > 3.4


def mostrar_menu(planetas):
    print("\n--- SISTEMA SOLAR ---")
    for i, planeta in enumerate(planetas, start=1):
        print(f"{i}. {planeta.nombre}")
    print(f"{len(planetas) + 1}. Salir")


if __name__ == "__main__":
    planetas = [
        Planeta("Mercurio", 0, 3.30e23, 6.08e10, 4879, 57.9, TipoPlaneta.TERRESTRE, True),
        Planeta("Venus", 0, 4.87e24, 9.28e11, 12104, 108.2, TipoPlaneta.TERRESTRE, True),
        Planeta("Tierra", 1, 5.97e24, 1.083e12, 12742, 149.6, TipoPlaneta.TERRESTRE, True),
        Planeta("Marte", 2, 6.42e23, 1.63e11, 6792, 227.9, TipoPlaneta.TERRESTRE, True),
        Planeta("Júpiter", 95, 1.90e27, 1.43e15, 139820, 778.5, TipoPlaneta.GASEOSO, True),
        Planeta("Saturno", 146, 5.68e26, 8.27e14, 116460, 1434.0, TipoPlaneta.GASEOSO, True),
        Planeta("Urano", 28, 8.68e25, 6.83e13, 50724, 2871.0, TipoPlaneta.GASEOSO, False),
        Planeta("Neptuno", 14, 1.024e26, 6.254e13, 49528, 4495.0, TipoPlaneta.GASEOSO, False)
    ]

    while True:
        mostrar_menu(planetas)
        opcion = input("\nSelecciona el número del planeta para ver su información: ")

        try:
            opcion_int = int(opcion)
            
            if 1 <= opcion_int <= len(planetas):
                planeta_elegido = planetas[opcion_int - 1]
                print(f"\n--- Información de {planeta_elegido.nombre} ---")
                planeta_elegido.mostrar_informacion()
                print(f"Densidad: {planeta_elegido.calcular_densidad():.2e} kg/km³")
                print(f"¿Es exterior?: {'Sí' if planeta_elegido.es_exterior() else 'No'}")
                input("\nPresiona Enter para continuar...")
                
            elif opcion_int == len(planetas) + 1:
                print("Cerrando la base de datos planetaria...")
                break
                
            else:
                print("Opción fuera de rango. Selecciona un número válido de la lista.")
                
        except ValueError:
            print("Error: Por favor, introduce únicamente valores numéricos.")}
