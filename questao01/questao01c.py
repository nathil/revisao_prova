#  Construa uma função com parâmetro arg. Retorne uma lista com todos registros em
# que alguma de suas informações tenha o valor do parâmetro arg como substring.

from questao01a import retorna_lista
import re

caminho = 'dados_usuario.txt'

#funções da questão
def retorna_todos_registros(arg: str) -> list:
    registros = retorna_lista(caminho)
    lista_substring = []

    for registro in registros: 
        for valor in registro.values(): 
            if bool(re.search(arg.lower(), valor.lower())):
                lista_substring.append(registro)    
                
                break

    return lista_substring

#Testes
print(retorna_todos_registros('aria'))

