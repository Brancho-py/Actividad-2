from enum import Enum

# Enumerado para el tipo de planeta
class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:
    #estarepresenta a un planeta dentro del sistema solar

    def __init__(self, nombre=None, cantidad_satelites=0, masa_kg=0.0, volumen_km3=0.0,
                diametro_km=0, distancia_media_sol_millones_km=0,
                tipo_planeta=TipoPlaneta.TERRESTRE, observable=False):
        """
        Constructor que inicializa todos los atributos del planeta.
        """
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa_kg = masa_kg
        self.volumen_km3 = volumen_km3
        self.diametro_km = diametro_km
        self.distancia_media_sol_millones_km = distancia_media_sol_millones_km
        self.tipo_planeta = tipo_planeta
        self.observable = observable

    def mostrar_informacion(self):
        #Imprime en pantalla todos los atributos del planeta.
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa (kg): {self.masa_kg}")
        print(f"Volumen (km³): {self.volumen_km3}")
        print(f"Diámetro (km): {self.diametro_km}")
        print(f"Distancia media al Sol (millones km): {self.distancia_media_sol_millones_km}")
        print(f"Tipo de planeta: {self.tipo_planeta.value}")
        print(f"Observable a simple vista: {'Sí' if self.observable else 'No'}")

    def calcular_densidad(self):
        """
        Calcula la densidad del planeta como masa / volumen.
        Si el volumen es cero, retorna infinito para evitar división entre cero.
        :return: float, densidad en kg/km³
        """
        if self.volumen_km3 == 0:
            return float('inf')
        return self.masa_kg / self.volumen_km3

    def es_exterior(self):
        """Determina si el planeta es exterior, es decir, si su distancia media al Sol
        en UA es mayor que 3.4 (más allá del cinturón de asteroides).
        Una UA equivale a 149 597 870 km.
        """
        # Convertir distancia de millones de km a km
        distancia_km = self.distancia_media_sol_millones_km * 1e6
        UA_en_km = 149597870
        distancia_ua = distancia_km / UA_en_km
        return distancia_ua > 3.4


if __name__ == "__main__":
    # Creación de dos planetas de ejemplo
    planeta1 = Planeta(
        nombre="Tierra",
        cantidad_satelites=1,
        masa_kg=5.97e24,
        volumen_km3=1.083e12,
        diametro_km=12742,
        distancia_media_sol_millones_km=149,
        tipo_planeta=TipoPlaneta.TERRESTRE,
        observable=True
    )

    planeta2 = Planeta(
        nombre="Neptuno",
        cantidad_satelites=14,
        masa_kg=1.024e26,
        volumen_km3=6.254e13,
        diametro_km=49528,
        distancia_media_sol_millones_km=4495,
        tipo_planeta=TipoPlaneta.GASEOSO,
        observable=False
    )

    # Mostrar información del primer planeta
    print("Información del Planeta 1:")
    planeta1.mostrar_informacion()
    print(f"Densidad: {planeta1.calcular_densidad():.2e} kg/km³")
    print(f"¿Es exterior? {'Sí' if planeta1.es_exterior() else 'No'}")
    print()

    # Mostrar información del segundo planeta
    print("Información del Planeta 2:")
    planeta2.mostrar_informacion()
    print(f"Densidad: {planeta2.calcular_densidad():.2e} kg/km³")
    print(f"¿Es exterior? {'Sí' if planeta2.es_exterior() else 'No'}")