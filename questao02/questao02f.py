# Utilizando o arquivo dados_DNA já atualizado com as duas novas colunas e utilizando
# a função que retorna a frequência máxima do padrão FREQ_ ATGCCA, construa uma
# função que retorne uma lista contendo os índices das linhas que possuem a FREQ_
# ATGCCA igual ao valor máximo.

from questao02e import retorna_freq
from questao02d import retorna_lista

caminho = 'novo_dados_DNA.txt'

def retorna_indice(caminho): 
    lista_seq = retorna_lista(caminho)
    freq_maxima = retorna_freq(caminho)
    lista_indices = []

    for item, seq in enumerate(lista_seq): 
        if seq['FREQ_ATGCCA'] == freq_maxima:
            lista_indices.append(item)

    return lista_indices

print(f'Lista de Índices:{retorna_indice(caminho)}')
