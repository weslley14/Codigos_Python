n = int(input('Digite um número inteiro qualquer: '))

while n != 0:
    ultimodigito = n % 10 #ultimo digito numero
    proximodigito = (n % 100) // 10 #proximo numero
   
    ncomultimo = n // 10
    n = ncomultimo

    if (ultimodigito == proximodigito):
        print('Esse número possui dígitos adjacentes iguais!')
        break
            
if (n == 0):
    print('Esse número não possui dígitos adjacentes iguais...')
