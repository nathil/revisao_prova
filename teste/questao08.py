# Você tem uma lista de dicionários onde cada dicionário contém o nome de um artigo e seu conteúdo. 
# Use map e regex para contar quantas vezes a palavra "Python" aparece em cada artigo (case-insensitive). 
# Retorne uma lista de dicionários com o nome do artigo e a contagem.

import re

caminho = 'questao08.csv'

def popular(): 
    
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write('nome,conteudo\n')
        arquivo.write('pesquisa programação,python pesquisa de python sobre python\n')
        arquivo.write('primeiros passos na programação,python um guia rapido\n') 

def retorna_lista(caminho):
    registros = []

    with open(caminho, 'r', encoding='utf-8') as arquivo: 
        dados = arquivo.readlines() 

    for dado in dados[1:]:
        valores = dado.strip().split(',')
        registro = {"nome": valores[0], "conteudo":valores[1]}
        registros.append(registro)
    
    return registros


retorna_nome_contagem = lambda caminho: list(map(lambda item: {'nome': item['nome'], 'contagem': len(re.findall(r'python', item['conteudo'], re.IGNORECASE))}, retorna_lista(caminho))) 

print(retorna_nome_contagem(caminho))