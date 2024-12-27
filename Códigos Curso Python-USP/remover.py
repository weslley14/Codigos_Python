def remove_repetidos(lista):
    lista_sem_repetidos = set(lista)
    lista_ordenada = sorted(lista_sem_repetidos)
    return lista_ordenada

numeros = [2,4,2,2,3,3,1]
resultado = remove_repetidos(numeros)
print(resultado)
