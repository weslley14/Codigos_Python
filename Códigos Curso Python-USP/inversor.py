def imprimir_inverso():
    numeros = []

    while True:
        numero = int(input("Digite um número (0 para terminar): "))
        if numero == 0:
            break
        numeros.append(numero)  

    for num in reversed(numeros):
        print(num)

imprimir_inverso()
