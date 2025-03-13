# crie uma função que receba uma lista de dicionários, onde cada dicionário tem os campos nome, genero, salario. 
# Cada dicionário representa um funcionário da empresa. A função deve aumentar em 20% o salário de todos os 
# funcionários do genero feminino. 

lista = [ {"nome": "maria", "genero": "F", "salario": 2000}
         ,{"nome": "ana clara", "genero": "F", "salario": 1600}
         ,{"nome": "davi", "genero": "M", "salario": 1000}] 

def funcao(item): 
    if item["genero"] == "F": 
        item["salario"] = (item["salario"]*20/100) + item["salario"]
    
    return item 

# def retorna_salario(lista):
#     nova_lista = []
    
#     for item in lista: 
#         novo_item = funcao(item) 
#         nova_lista.append(novo_item)

#     return nova_lista

def retorna_salario(lista):
    nova_lista = list(map(funcao, lista))
    return nova_lista

print(retorna_salario(lista))

