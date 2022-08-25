##Ingresar un numero y definir si es un numero primo o no
def primo(num):
    if num == 0 or num == 1 or num == 4:
        return False
    for a in range(2, int(num/2)):
        if num % a == 0:
            return False
    return True
num = int(input("Ingrese el numero a evaluar: "))
es_primo = primo(num)
if es_primo:
	print("El numero que usted ingreso ES PRIMO")
else:
	print("El numero que usted ingreso NO ES PRIMO")