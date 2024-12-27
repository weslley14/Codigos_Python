#n = int(input('Digite um número: '))
#k = int(input('Digite um número: '))

def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

def binominal(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))

def testa_binominal():
    if binominal(12, 10) == 66:
        print("Funciona para n = 12 e k = 10")
    else:
        print("Não funciona para n = 12 e k = 10")
    if binominal(4, 0) == 1:
        print("Funciona para n = 4 e k = 0")
    else:
        print("Não funciona para n = 4 e k = 0")
    if binominal(4, 2) == 6:
        print("Funciona para n = 4 e k = 2")
    else:
        print("Não funciona para n = 4 e k = 2")
    if binominal(10, 3) == 120:
        print("Funciona para n = 10 e k = 3")
    else:
        print("Não funciona para n = 10 e k = 3")
