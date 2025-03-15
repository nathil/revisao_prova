# Calcular a Média Ponderada Você tem uma lista de dicionários onde cada 
# dicionário representa uma nota e seu peso. Use reduce para calcular a média ponderada das nota


from functools import reduce

notas = [
    {"nota": 8, "peso": 2},
    {"nota": 7, "peso": 3},
    {"nota": 9, "peso": 1},
    {"nota": 6, "peso": 4}
]

# def soma(soma, item): 
#     soma = (item["nota"] * item["peso"]) + soma
#     return soma

# def soma_pesos(soma_pesos, item): 
#     soma_pesos = item["peso"] + soma_pesos
#     return soma_pesos

# f_soma = lambda soma, item: soma + (item["nota"] * item["peso"])
# f_soma_pesos = lambda soma_pesos, item: soma_pesos + item["peso"]

def calcular_media(notas_lista: float) -> float:
    
    soma = reduce(lambda soma, item: soma + (item["nota"] * item["peso"]), notas_lista, 0)
    soma_pesos = reduce(lambda soma_pesos, item: soma_pesos + item["peso"], notas_lista, 0)

    media = soma/soma_pesos
    return media

print(f'{calcular_media(notas)}')