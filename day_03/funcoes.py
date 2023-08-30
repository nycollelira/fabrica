def soma (x: int | float, y : int | float) -> int | float:
    "soma x e y e retorna o resultado"
    #resultado = x + y
    return x + y

def print_subtracao (x: int | float , y : int | float ) -> None:
    "subtrai x - y e mostra o resultado o print"
    print(f"resultado: {x - y}")

def soma_sem_parametro() -> int | float:
    x = 5
    y = 5
    return x + y
