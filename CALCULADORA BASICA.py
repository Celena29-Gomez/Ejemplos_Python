for  a in range (10):
 print ("CALCULADORA")
 print ("Menu - OPCIONES")
 print ("1 Suma")
 print ("2 Resta")
 print ("3 Multiplicacion")
 print ("4 Division")
 print ("5 Salir")
 opcion=int(input("Que operacion desea hacer? Ingrese su opcion a calcular: "))
 if opcion == 5:
        print("GRACIAS POR HACER USO DE MI CALCULADORA DE OPERACIONES BASICAS")
 else:
        a=int(input("Ingrese el primer numero para calcular: "))
        b=int(input("Ingrese el segundo numero para calcular: "))
        if opcion==1:
            print("El resultado de la suma es ", a+b)
        elif opcion==2:
            print("El resultado de la resta es ", a-b)
        elif opcion==3:
            print("El resultado de la multiplicacion es ", a*b)
        elif opcion==4:
            print("El resultado de la division es ",a/b)