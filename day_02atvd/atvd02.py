num1 = input("qual número deseja? ") 
antecessor = 0
sucessor = 0

try: 
    antecessor = int(num1) -1
    sucessor = int(num1) +1
except ValueError:
    raise ValueError("Digite um número válido")
    print("Digite um número válido")
    
print(f"O número digitado foi {num1} e seu antecessor é {antecessor} e o sucessor {sucessor}")

print(type(num1))
print(type(antecessor))
print(type(sucessor))