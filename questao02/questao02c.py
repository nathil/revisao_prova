# Considerando o arquivo dados_DNA, construa uma função que leia os registros e,
# para cada registro, utilizando as funções das questões anteriores, passe os argumentos
# de forma nomeada, tal que, a cadeia corresponde a linha do arquivo e o padrao deve
# ser ATGCCA. Utilize o retorno das funções para criar e preencher, no arquivo
# dados_DNA, as colunas:
# ● FREQ_ATGCCA
# ● TEM_ ATGCCA

from questao02a import qtd_repeticao
from questao02b import padrao_presente

caminho = 'dados_DNA.txt'

def funcao(caminho): 
    padrao = 'ATGCCA'

    with open(caminho, 'r', encoding='utf-8') as arquivo:
        cadeias = arquivo.readlines()
    
    with open('novo_'+caminho, 'w', encoding='utf-8') as arquivo: 
        arquivo.write('FREQ_ATGCCA,TEM_ATGCCC\n')
    
    for cadeia in cadeias[1:]:    
        quantidade_repeticao = qtd_repeticao(cadeia,padrao)
        padraoo_presente = padrao_presente(cadeia,padrao) 
        registro = f'{quantidade_repeticao},{padraoo_presente}\n'
        
        with open('novo_'+caminho, 'a', encoding='utf-8') as arquivo: 
            arquivo.write(registro)

funcao(caminho)


