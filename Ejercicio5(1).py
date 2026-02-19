class CuentaBancaria:
    def __init__(self,nombre_titular,apellidos_titular,numero_cuenta,tipo_cuenta,saldo):
        self.nombre = nombre_titular
        self.apellidos = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo

    def atributos(self):
        print(f"Nombre del titular: {self.nombre}")
        print(f"Apellidos del titular: {self.apellidos}")
        print(f"Numero de cuenta: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta}")
        print(f"Saldo: {self.saldo}$")
        print()

    def consultar_saldo(self):
        print(f"Su saldo actual es: {self.saldo}$")
        
    
    def retirar_valor(self):
        valor_retirar = float(input("Ingrese el valor que desea retirar: "))
        if valor_retirar > self.saldo:
            print("Usted no tiene saldo suficiente, vuélvalo a intentar")
            return 
        elif valor_retirar < 0:
            print("No es válido")
            return
        else:
            self.saldo -= valor_retirar
            print("Se ha retirado con éxito")
            return self.saldo
    
    def consignar_valor(self):
        valor_consignar = float(input("Cuanto desea consignar?: "))
       
        if valor_consignar < 0:
            print("No es válido")
            return
        self.saldo += valor_consignar
        print("Se ha consignado el valor con éxito")
        return self.saldo


def menu():
    cuenta1 = crear_cuenta()
    while True:
       print(f"Hola {cuenta1.nombre} {cuenta1.apellidos} este es el menú de su cuenta de banco, que desea hacer?\n")
       print("(1) Consignar un valor")
       print("(2) Retirar un valor")
       print("(3) Consultar saldo")
       print("(4) Ver todos mis datos")
    
       opcion = float(input("Ingrese el numero de la opcion que desea: "))
       print()
       if opcion > 4 or opcion < 1:
          print("Opción inválida, vuelvalo a intentar")

       elif opcion == 1:
           cuenta1.consignar_valor()

       elif opcion == 2:
           cuenta1.retirar_valor()

       elif opcion == 3:
           cuenta1.consultar_saldo() 

       elif opcion == 4:
           cuenta1.atributos()

cuentas = []

def crear_cuenta():
    
    print("Cree su cuenta bancaria\n")
    nombre = input("Ingrese su nombre: ")
    apellidos = input("Ingrese sus apellidos: ")
    numero_cuenta = len(cuentas) + 1
    tipo_cuenta = input("Desea que su cuenta sea corriente o ahorros?: ")
    saldo = 0
    cuenta = CuentaBancaria(nombre,apellidos,numero_cuenta,tipo_cuenta,saldo)
    cuentas.append(cuenta)

    return cuenta




menu()
           
