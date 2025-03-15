from functools import reduce

caminho = 'arquivo2.csv'

def retorna_lista(caminho): 
    registros = []

    with open(caminho, 'r', encoding='utf-8') as arquivo:
        dados = arquivo.readlines()

    for dado in dados[1:]:
        valores = dado.strip().split(',')
        registro = {'Codigo': valores[0], 'Tipo': valores[1], 'Validade': valores[3], 'Quantidade':int(valores[4])}
        registros.append(registro)
    
    return registros



# def quantidade_de_carga_por_tipo(lista_cargas, cod_setor):
#     lista_cargas = retorna_lista(caminho)

#     dicionario = {}

#     for carga in lista_cargas: 
#         if cod_setor == carga['Codigo'][:2]:
#             if carga['Tipo'] in dicionario: 
#                 dicionario[carga['Tipo']] += carga['Quantidade']
#             else: 
#                 dicionario[carga['Tipo']] = carga['Quantidade']
        
#     return dicionario


def quantidade_de_carga_por_tipo(lista_cargas, cod_setor):
    lista_cargas = retorna_lista(caminho)
    
    def funcao(dicionario, item):
        if cod_setor == item['Codigo'][:2]:
            if item['Tipo'] in dicionario: 
                dicionario[item['Tipo']] += item['Quantidade']
            else: 
                dicionario[item['Tipo']] = item['Quantidade']
        
        return dicionario

    dicionario = reduce(funcao, lista_cargas,{})
        
    return dicionario

lista_cargas = retorna_lista(caminho)

print(quantidade_de_carga_por_tipo(lista_cargas,'AO'))

