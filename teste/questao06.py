# Questão 1: Criar um Relatório de Emails Válidos e Inválidos
# Você tem uma lista de dicionários onde cada dicionário contém o nome e o email de uma pessoa. 
# Use filter e regex para separar os emails válidos dos inválidos. 
# Retorne um dicionário com duas chaves: "validos" e "invalidos", contendo listas com os respectivos emails.

import re

caminho = 'questao06.csv'

#funções essenciais

def popular(caminho): 
    with open(caminho, 'w', encoding='utf-8') as arquivo: 
        arquivo.write(f'nome,email\n') 
        arquivo.write(f'maria,maria202@gmail.com\n')
        arquivo.write(f'antonia,antoniatonia.rosa@gmail.com\n')
        arquivo.write(f'roberto,.123asgmail.com\n') 
        arquivo.write(f'davi josé,davii_2000@yahoo.com\n') 


def retorna_lista(caminho):
    try:
        registros = []

        with open(caminho, 'r', encoding='utf-8') as arquivo: 
            dados = arquivo.readlines() 
        
        for dado in dados[1:]: 
            valores = dado.strip().split(',')
            registro = {"nome": valores[0], "email": valores[1]}
            registros.append(registro) 
        
        return registros
    
    except FileNotFoundError:
        print("O arquivo não existe!")

#funções

# def validos(item):
#     if bool(re.fullmatch(r'[a-zA-Z]\w{4,}@[a-zA-Z]{4,}\.[a-zA-Z]{1,6}(\.[a-zA-Z]{1,3})?', item['email'])):
#         return True
#     return False
    
validos = lambda item: bool(re.fullmatch(r'[a-zA-Z]\w{4,}@[a-zA-Z]{4,}\.[a-zA-Z]{1,6}(\.[a-zA-Z]{1,3})?', item['email']))
invalidos = lambda item: not bool(re.fullmatch(r'[a-zA-Z]\w{4,}@[a-zA-Z]{4,}\.[a-zA-Z]{1,6}(\.[a-zA-Z]{1,3})?', item['email']))

def mapeamento(item): 
    return item["email"] 

def funcao(caminho): 
    registros = retorna_lista(caminho)
    
    lista_validos = list(map(mapeamento, (filter(validos, registros))))   
    lista_invalidos = list(map(mapeamento,(filter(invalidos, registros))))

    dicionario = {"validos": lista_validos, "invalidos": lista_invalidos}

    return dicionario 

print(funcao(caminho))

            
