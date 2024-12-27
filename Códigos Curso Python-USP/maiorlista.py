def maior_elemento(lista):
    if not lista:  
        return None

    maior = lista[0]  
    for num in lista:
        if num > maior:
            maior = num  
    return maior

numeros = [5,2,1,7,4]
print(maior_elemento(numeros))
