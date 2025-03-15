# Write a Python program to listify the list of given strings individually using Python map and lambda.

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]

# com lambda

def soma(lista1, lista2, lista3):
    nova_lista = list(map(lambda item: sum(item), zip(lista1, lista2, lista3)))
    return nova_lista


# com map 
# def funcao(item): 
#     soma = sum(item)
    
#     return soma

# def soma(lista1, lista2, lista3):
#     nova_lista = list(map(funcao, zip(lista1, lista2, lista3)))
#     return nova_lista

#forma estruturada

# def soma(lista1, lista2, lista3):
#     nova_lista = []
    
#     for item1, item2, item3 in zip(lista1, lista2, lista3): 
#         soma = sum([item1, item2, item3])
#         nova_lista.append(soma)
#     return nova_lista

print(soma(lista1, lista2, lista3))