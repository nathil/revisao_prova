# Desenvolva um programa que apresente a soma dos valores
# pares e dos valores ímpares da sequência ([21, 5, 34, 8, 16, 7, 3])

def soma_pares(lista):
    soma_pares = 0

    for item in lista: 
        if item % 2 == 0:
            soma_pares += item
    return soma_pares

lista = [21, 5, 34, 8, 16, 7, 3]

print(f'soma pares:{soma_pares(lista)}')