# Write a Python program to listify the list of given strings individually using Python map.

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]

def soma(lista1, lista2, lista3):
    nova_lista = []
    
    for item1, item2, item3 in zip(lista1, lista2, lista3): 
        soma = sum([item1, item2, item3])
        nova_lista.append(soma)
    return nova_lista

print(soma(lista1, lista2, lista3))