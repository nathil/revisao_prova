from questao01 import retorna_lista 
from functools import reduce

caminho = 'arquivo.csv'

lista = retorna_lista(caminho)

# def retorna_idade(caminho):

#     qdt_F = 0 
#     qdt_M = 0 
#     soma_F = 0 
#     soma_M = 0 

#     for item in lista:
#         if item['Sexo'] == 'F':
#             qdt_F += 1
#             idade = 2025 - int(item['Ano_nascimento'])
#             soma_F = idade + soma_F 
        
#         if item['Sexo'] == 'M':
#             qdt_M += 1
#             idade = 2025 - int(item['Ano_nascimento'])
#             soma_M = idade + soma_M
    
#     media_F = soma_F/qdt_F
#     media_M = soma_M/qdt_M
    
#     return media_F, media_M


def idade_f(soma_qdt_F, item):
    soma_F,qdt_F = soma_qdt_F

    if item['Sexo'] == 'F':
        qdt_F += 1
        idade = 2025 - int(item['Ano_nascimento'])
        soma_F = idade + soma_F 
    
    return soma_F, qdt_F

def idade_m(soma_qdt_M, item):
    soma_M, qdt_M = soma_qdt_M

    if item['Sexo'] == 'M':
        qdt_M += 1
        idade = 2025 - int(item['Ano_nascimento'])
        soma_M = idade + soma_M
    
    return soma_M, qdt_M

def retorna_idade(caminho):
        
    soma_F, qdt_F = reduce(idade_f, lista, (0,0))
    soma_M, qdt_M = reduce(idade_m, lista, (0,0))
    
    media_F = soma_F/qdt_F
    media_M = soma_M/qdt_M
    
    return media_F, media_M


media_F, media_M = retorna_idade(caminho)

print(f'A media de idade de mulheres é:{media_F}\nA media de idades de homens é:{media_M}')