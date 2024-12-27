entrada=input("Por favor, entre com o número de segundos que deseja converter: ")
tempo=int(entrada)


dia = tempo // 86400
t = tempo % 86400
horas = t // 3600
tempo_restante= tempo % 3600
minutos = tempo_restante // 60
segundos = tempo_restante % 60

print(dia,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
