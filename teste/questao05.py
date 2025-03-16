
from questao01 import retorna_lista 
import re 

caminho = 'arquivo.csv' 

def filtro(item):
    if (bool(re.fullmatch(r'[a-zA-Z]\w{4,}@[a-zA-Z]{4,}\.[a-zA-Z]{1,6}(\.[a-zA-Z]{1,3})?',item['E-mail']))):
        return True
    return False 

def mapeamento(item): 
    return item['Nome'], item['Ano_nascimento']

def funcao(caminho):
    lista_registros = retorna_lista(caminho)
    lista_nome_ano = filter(filtro, lista_registros) 
    lista_nome_ano = list(map(mapeamento, lista_nome_ano)) 
    
    return lista_nome_ano

def retorna_nome_ano(caminho):
    lista_registros = retorna_lista(caminho) 
    lista_nome_ano = []
#\w dá match em letras, números ou _ 
    for registro in lista_registros:
        if bool(re.fullmatch(r'[a-zA-Z]\w{4,}@[a-zA-Z]{4,}\.[a-zA-Z]{1,6}(\.[a-zA-Z]{1,3})?', registro['E-mail'])):
            lista_nome_ano.append((registro['Nome'],registro['Ano_nascimento']))
    
    return lista_nome_ano

print(funcao(caminho))