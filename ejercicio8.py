dinero = float(input("Ingrese su cantidad de dinero: "))
años = int(input("Ingrese los años a ahorrar: "))
interes = 4
total =dinero +(dinero*años*interes)/100 
print("Su dinero ahorrado es: "+ str(total))