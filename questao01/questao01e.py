# Construa uma função para salvar novos registros. A função deve ter os parâmetros
# nome, ano sexo, numero. O ID deve ser gerado automaticamente sendo igual ao valor
# do último ID registrado + 1.

from questao01a import retorna_lista

caminho = 'dados_usuario.txt'

def salvar_registro(nome, ano, sexo, numero):
    registros = retorna_lista(caminho)

    ultimo_id = registros[-1]['ID']  
    id = str(int(ultimo_id)+1) 
    registro = f'{id},{ano},{sexo},{nome},{numero}\n'

    with open(caminho, 'a', encoding='utf-8') as arquivo:
        arquivo.write(registro)


salvar_registro('Dora','2001','F','(91) 988765498')