# Desenvolva um programa que converta todas as temperaturas desta 
# lista em Celsius [22.5, 40, 13, 29, 34] para Fahrenheit

def funcao(item: float) -> float: 
    return (item*1.8) + 32  
    
def retorna_fahrenheit(funcao, lista):
    nova_lista = [] 

    for item in lista: 
        novo_item = funcao(item)
        nova_lista.append(novo_item)
    
    return nova_lista


#com map 

# def retorna_fahrenheit(lista):
#     nova_lista = list(map(funcao, lista))
#     return nova_lista

lista = [22.5, 40, 13, 29, 34]

print(f'{retorna_fahrenheit(funcao, lista)}')
# print(f'{retorna_fahrenheit(lista)}')




