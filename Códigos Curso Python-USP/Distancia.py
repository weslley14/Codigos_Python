import math

x = float(input("Digite o primeiro ponto da coordenada X:"))
y = float(input("Digite o primeiro ponto da coordenada Y:"))
x1 = float(input("Digite o segundo ponto da coordenada X:"))
y1 = float(input("Digite o segundo ponto da coordenada X:"))

n = (x - x1) ** 2 + (y - y1) ** 2  

d = math.sqrt(n)

if d >= 10 :
    print("longe")

else:
    print("perto")
