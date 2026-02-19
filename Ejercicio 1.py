class Persona:
    def __init__(self,nombre,apellido,cedula,fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento

    def atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Cedula: {self.cedula}")
        print(f"Fecha nacimiento: {self.fecha_nacimiento}")

personas = [] 

veces = int(input("Cuantas personas quiere añadir?: "))
for i in range (veces):
    nom = input("Ingrese el nombre de la persona: ")
    ape = input("Ingrese el apellido de la persona: ")
    ide = input("Ingrese la cedula de la persona: ")
    fecha = input("Ingrese la fecha de nacimiento de la persona: ")
    persona_n = Persona(nom,ape,ide,fecha)
    personas.append(persona_n)

for p in personas:
    p.atributos()
    print()


    
        

