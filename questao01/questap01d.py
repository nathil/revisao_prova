# Construa uma função com o parâmetro numero. Retorne uma lista com os Ids dos
# registros que possuem o number igual ao valor do parâmetro numero.

from questao01a import retorna_lista
import re

caminho = 'dados_usuario.txt'


#funções da questão
def retorna_ids(numero : str) -> list: 
    registros = retorna_lista(caminho)
    lista_ids = []

    for registro in registros: 
        if numero == registro['Number']:
            lista_ids.append(registro['ID'])

    return lista_ids

#Testes
# if __name__ == '__main__':
print(f"Lista de IDs:{retorna_ids('(91) 976895436')}")
