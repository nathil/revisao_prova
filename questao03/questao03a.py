def primos_entre_si(valor1: int, valor2: int) -> bool:
    
    menor = min(valor1, valor2)

    for i in range(2, menor + 1):
        if valor1 % i == 0 and valor2 % i == 0:
            return False
    return True

print(primos_entre_si(12,25))