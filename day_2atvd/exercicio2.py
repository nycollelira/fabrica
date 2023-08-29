velocidade = input("Digite sua velocidade: ")
velcidade_int = 0

try:
    velocidade_int = int(velocidade)
except ValueError:
    raise ValueError("Digite a velocidade em números")

if velocidade_int < 80:
    print("Você esta na velocidade da via")
elif velocidade_int == 80:
    print("Você atingiu a velocidade limite")
else:
    print(f"Você está acima do limite da via e sua multa foi de {(velocidade_int - 80) * 7 };00 reais")