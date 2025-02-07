

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y



while True:

    print("Elige la operacion")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")

    eleccion = input("Elige tu opcion(1/2/3/4): ")

    if eleccion in ('1', '2', '3', '4'):
        num1 = float(input("Pon el primer numero: "))
        num2 = float(input("Pon el segundo numero: "))

        if eleccion == '1':
            print(num1, "+", num2, "=", sumar(num1, num2))

        elif eleccion == '2':
            print(num1, "-", num2, "=", restar(num1, num2))

        elif eleccion == '3':
            print(num1, "*", num2, "=", multiplicar(num1, num2))

        elif eleccion == '4':
            print(num1, "/", num2, "=", dividir(num1, num2))
        
        siguienteCalculo = input("Quieres cambiar de operacion?? (s/n): ")
        if siguienteCalculo == "no":
          break
    
    else:
        print("Entrada invalida, invalido")