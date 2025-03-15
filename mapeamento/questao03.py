# Desenvolva um programa que apresente a soma dos valores
# pares e dos valores ímpares da sequência ([21, 5, 34, 8, 16, 7, 3])

from functools import reduce

#forma estruturada

# def f_par(soma, item): 
#     if item % 2 == 0: 
#         soma += item 
#     return soma

f_par = lambda soma, item: soma + item if item % 2 == 0 else soma
f_impar = lambda soma, item: soma + item if item % 2 != 0 else soma

def soma(lista):
    soma_pares = reduce(f_par, lista, 0)
    soma_impares = reduce(f_impar, lista, 0)

    return soma_pares, soma_impares
 
# def soma_pares(lista):
#     soma_pares = 0
#     for item in lista: 
#         soma_pares = f_par(soma_pares, item)
#     return soma_pares

# def f_impar(soma, item): 
#     if item % 2 != 0:
#         soma += item 
#     return soma

# def soma_impares(lista):
#     soma_impares = 0 

#     for item in lista: 
#         soma_impares = f_impar(soma_impares, item)
#     return soma_impares


lista = [21, 5, 34, 8, 16, 7, 3]
soma_pares, soma_impares = soma(lista)

print(f'soma pares:{soma_pares}\nsoma impares:{soma_impares}')