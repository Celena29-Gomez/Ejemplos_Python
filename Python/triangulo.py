## un algoritmo para idetificar que tipo de triangulo es a partir de recibir los 3 lados
## ejemplo si recibe 3  3   3 debe retornar que es un triangulo equilatero
lado1 = float(input("Ingrese el Valor del primer lado:"))
lado2 = float(input("Ingrese el Valor del segundo lado:"))
lado3 = float(input("Ingrese el Valor del tercer lado:"))
if(lado1==lado2 and lado2==lado3):
    print ("Segun el valor de cada lado ingresado es un  Triangulo es Equilatero")
elif(lado1==lado2 or lado1==lado3 or lado2==lado3):
    print ("Segun el valor de cada lado ingresado es un Triangulo es Isoceles")
elif (lado1!=lado2 or lado1!=lado3 or lado2!=lado3):
    print ("Segun el valor de cada lado ingresado es un  Triangulo es Escaleno")