nombre_cliente= input("INGRESE SU NOMNRE: ")
precio = input("ingrese el precio: ")
cantidad = input("cantidad de productos: ")
cliente_vip1 = input("es cleinte vip?: ")
cliente_vip = bool
cantidad=float(cantidad)
precio=float(precio)
subtotal = precio * cantidad
try:
 if (cliente_vip):
    descuento = subtotal * 0.10
 else:
    cliente_vip =bool
    print("no aplpica")
 subtotalf2 = subtotal - descuento
except: print("no es un numero")
print("cliente :",nombre_cliente)
print("total:", subtotal)
print("descuento: ",descuento)
print("total a pagar: ",subtotalf2)
