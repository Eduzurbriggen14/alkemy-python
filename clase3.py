def accion_a(num1 , num2):
    return num1 + num2
    

def accion_b(num1, num2):
    return num1 - num2
     


def programa():    
    print("ingrese el numero 1 para realizar la suma de dos numeros")

    print("ingrese el numero 2 para realizar la resta de dos numeros")
    print("--------------")

    opcion = int(input("ingrese el numero 1 o 2 para realizar una operacion: "))
    num1 = int(input("ingrese el primer numero entero: "))
    num2 = int(input("ingrese el segundo numero entero: "))

    if(opcion == 1):
        resultado = accion_a(num1, num2)
        print(f"el resultado es : {resultado}")

    elif(opcion == 2):
        resultado = accion_b(num1, num2)
        print(f"el resultado es : {resultado}")

    else:
        print("la opcion ingresada no es valida ")


programa()