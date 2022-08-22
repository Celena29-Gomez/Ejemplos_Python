#Pedir un numero y mostrar por pantalla si ese numero es par o impar 
for  a in range (15):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        print("El numero que usted ingreso es par")
    else:
        print("El numero que usted ingreso es impar")
    if numero == 0:
        print ("El numero que usted ingreso es cero")
