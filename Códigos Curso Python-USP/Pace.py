x = input("Digite a metragem em metros: ")
y = input("Digite os minutos: ")
z = input("Digite os segundos: ")

m = int(x)
Rec = int(y)
Rec1 = int(z)

Min= Rec * 60
seg= Rec1 + Min

mult = 100 * seg / m
red = mult / 60
minutos = int(mult // 60)
segundos = int(mult % 60)

#print(Min, seg, mult, red, minutos, segundos)
print("Seu tempo a cada 100m foi de", minutos, "minutos e", segundos, "segundos.")
