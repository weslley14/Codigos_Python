n = int(input("Digite o valor de n: "))

n=n*2
x = 0

while x < n:
    x = (x + 1)
    if x % 2 != 0:
        print(x)
