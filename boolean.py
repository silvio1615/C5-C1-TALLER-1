
puede_conducir = True
edad = input("ingresa edad") 

try:
 
    edad = int(edad)
    print("el dato ingresado es un numero")
    if edad >= 26: 
        print("tiene permiso para conducir")
    
    else:
        print("no tiene permiso para cundicir ")
        puede_conducir = False


    if (puede_conducir):
        print("se comfirma que usted puede conducir")

except:
    print("el Dato ingresado no es un numero") 

     
  