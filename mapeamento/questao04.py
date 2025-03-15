# Write a Python program to triple all numbers in a given list of integers. Use Python map.

def funcao(item):
    return item*3

def retorna_valores(funcao, lista):
    nova_lista = list(map(funcao, lista))
    return nova_lista

lista = [1,2,3,4,5,6,7,8,9,10]

print(f'Nova lista:{retorna_valores(funcao, lista)}')
