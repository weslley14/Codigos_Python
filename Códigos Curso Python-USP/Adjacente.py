n = int(input('Digite um número inteiro: '))

while n != 0:
    lastDigit = n % 10
    beforeLastDigit = (n % 100) // 10

    numberWithoutLastDigit = n // 10
    n = numberWithoutLastDigit

    if (lastDigit == beforeLastDigit):
        print('sim')
        break
            
if (n == 0):
    print('não')
