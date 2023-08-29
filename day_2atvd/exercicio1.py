nome= input("digite seu nome: ")
idade= input("digite sua idade: ")

idade_int = 0
try:
    idade_int = int(idade)
except ValueError:
    raise ValueError('Digite a idade em números')

if idade < 18:
    print(f'Desculpe {nome} mas a idade minima para obter a carteira de motorista é de 18 anos')
else:
    print(f'Parabéns {nome} você esta apto para podere tirar sua carteira de morotista')                                      