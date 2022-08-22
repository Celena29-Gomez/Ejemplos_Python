#fibonacci
def fibonacci (n):
    x = 0
    y = 1
    
    for k in range (n):
        z = x+y
        x = y
        y = z 
    return y   
cant = int(input("Ingrese cantidad de numeros a cargar: "))
for a in range (cant):
    print (fibonacci(a))