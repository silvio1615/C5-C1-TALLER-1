print("menu de opciones: ")
print("1. consultar saldo")
print("2. retirar dinero")
print("3. depositar dinero")
saldo_inicial = 1000.0
opcion = int(input("elija una opcion (1-3): "))
if opcion == 1:
    print("su saldo actual es: ",saldo_inicial)
elif opcion == 2:
    retirar_dinero = float(input("cuanto desea retirar?:"))

elif opcion == 3:
   def depositar(cantidad):
    if cantidad>saldo_inicial :
     saldo_inicial+=cantidad
     print(f"su nuevo saldo es:",cantidad)
