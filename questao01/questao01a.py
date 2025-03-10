# Construa uma função com o parâmetro nome. Retorne a quantidade e uma lista com
# os registros cujo nome inicie com o valor do parâmetro nome. Se nenhum argumento
# for passado para o parâmetro nome, então considere como valor default uma string
# vazia.

import re

caminho = 'dados_usuario.txt'

#funções essenciais

def popular_arquivo() -> None:
    with open(caminho, 'w', encoding='utf-8') as arquivo: 
        arquivo.write('ID,year,gender,name,number\n')
        arquivo.write('1,2006,M,José Henrique,(91) 987679045\n')
        arquivo.write('2,1986,F,Marian,(91) 976895436\n')
        arquivo.write('3,2000,M,Murilo,(91) 989764587\n')


def retorna_lista(caminho: str) -> list:
    registro = []
    registros = []

    with open(caminho, 'r', encoding='utf-8') as arquivo: 
        dados = arquivo.readlines() 
    
    for dado in dados[1:]: 
        valores = dado.strip().split(',')
        registro = {'ID': valores[0], 'Year': valores[1], 'Gender': valores[2], 'Name': valores[3], 'Number': valores[4]} 
        registros.append(registro)
    
    return registros


#funções das questões 

def retorna_quantidade_nome(nome = '') -> tuple:
    """Retorna a quantidade de nomes que começam com o parâmetro inserido. 
    """
    registros = retorna_lista(caminho) 
    registros_nome = []
    qtd = 0

    for registro in registros: 
        if bool(re.match(nome.lower(), registro['Name'].lower())):
            qtd += 1
            registros_nome.append(registro)
    
    return registros_nome, qtd 

#Testes
popular_arquivo()

lista_nomes, qdt = retorna_quantidade_nome('M')
print(f"Lista de Nomes:{lista_nomes}\nQuantidade dos Nomes:{qdt}")
