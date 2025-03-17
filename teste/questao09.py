# Questão 5: Validar e Classificar Senhas Você tem uma lista de dicionários onde cada dicionário contém
# o nome de um usuário e sua senha. Use filter e regex para classificar as senhas em "fortes" e "fracas". 
# Uma senha é considerada forte se tiver pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, 
# um número e um caractere especial.

import re

caminho = 'questao09.csv' 

def popular(): 
    with open(caminho, 'w', encoding='utf-8') as arquivo: 
        arquivo.write(f'nome,usuario,senha\n')
        arquivo.write(f'murilo,lilo12,123456\n')
        arquivo.write(f'nath,lily,98981231Nm!\n')

popular()


def retorna_lista(caminho): 
    registros = []

    with open(caminho, 'r', encoding='utf-8') as arquivo: 
        dados = arquivo.readlines() 
    
    for dado in dados[1:]: 
        valores = dado.strip().split(',')
        registro = {"Nome": valores[0], "Usuario": valores[1], "Senha": valores[2]}
        registros.append(registro) 
    
    return registros

filtrar_fortes = lambda item: all([bool(re.search(r'[a-z]', item['Senha'])), bool(re.search(r'[A-Z]', item['Senha'])), bool(re.search(r'[0-9]', item['Senha'])), bool(re.search(r'[!@#$%&*]', item['Senha']))])
filtrar_fracas = lambda item: not all([bool(re.search(r'[a-z]', item['Senha'])), bool(re.search(r'[A-Z]', item['Senha'])), bool(re.search(r'[0-9]', item['Senha'])), bool(re.search(r'[!@#$%&*]', item['Senha']))])

senha_forte = lambda caminho: {'Fortes': list(filter(filtrar_fortes, retorna_lista(caminho))), 'Fracas': list(filter(filtrar_fracas, retorna_lista(caminho)))}

print(senha_forte(caminho))
