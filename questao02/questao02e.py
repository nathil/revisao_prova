# Utilizando o arquivo dados_DNA já atualizado com as duas novas colunas, construa
# uma função que retorne a frequência máxima que o padrão ATGCCA na base de dados.
# Para isso, você deve utilizar os dados da coluna FREQ_ ATGCCA

from questao02d import retorna_lista

caminho = 'novo_dados_DNA.txt'

def retorna_freq(caminho):
    lista_seq = retorna_lista(caminho)

    maior = lista_seq[0]['FREQ_ATGCCA']
    for seq in lista_seq: 
        if seq['FREQ_ATGCCA'] > maior: 
            maior = seq['FREQ_ATGCCA']
    
    return maior

print(f'A frequência máxima é de:{retorna_freq(caminho)}')

#refazer depois com o reduce 