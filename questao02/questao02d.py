# Utilizando o arquivo dados_DNA já atualizado com as duas novas colunas, construa
# uma função que retorne a quantidade de sequências que não possui o padrão ATGCCA.
# Para isso, você deve utilizar os dados da coluna TEM_ ATGCCA

caminho = 'novo_dados_DNA.txt'


def retorna_lista(caminho): 
    lista_seq = []

    with open(caminho, 'r', encoding='utf-8') as arquivo: 
        dados = arquivo.readlines()

    for dado in dados[1:]:
        valores = dado.strip().split(',')
        registro = {'FREQ_ATGCCA': valores[0], 'TEM_ ATGCCA': valores[1]}
        lista_seq.append(registro)
    
    return lista_seq
        

def retorna_qtd(caminho):
    lista_seq = retorna_lista(caminho)
    qdt = 0 

    for seq in lista_seq: 
        if seq['TEM_ ATGCCA'] == 'False':
            qdt += 1
    return qdt


print(retorna_qtd(caminho))