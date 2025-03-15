from functools import reduce

caminho = 'arquivo.csv'

def retorna_lista(caminho):
    registros = []

    with open(caminho, 'r', encoding='utf-8') as arquivo:
         dados = arquivo.readlines() 
    
    for dado in dados[1:]:
         valores = dado.strip().split(',')
         registro = {'Nome':valores[0], 'Telefone': valores[1], 'E-mail': valores[2], 'CPF': valores[3]
                     ,'Ano_nascimento': valores[4], 'Sexo': valores[5], 'UF': valores[6], 'Cidade':valores[7]}
         registros.append(registro)     
    
    return registros


def retorna_uf_qtd(dicionario, item): 
    if item['E-mail'] == '':
        if item['UF'] in dicionario:
            dicionario[item['UF']] += 1
        else: 
            dicionario[item['UF']] = 1
    return dicionario
    

def registro_sem_email(caminho):
    registros = retorna_lista(caminho)

    registro_sem_email = reduce(retorna_uf_qtd, registros, {})
    
    return registro_sem_email

# def registro_sem_email(caminho):
#     registros = retorna_lista(caminho)
#     registro_sem_email = {}

#     for registro in registros: 
#          if registro['E-mail'] == '':  
#             if registro['UF'] in registro_sem_email:
#                 registro_sem_email[registro['UF']] += 1
#             else:
#                  registro_sem_email[registro['UF']] = 1
    
#     return registro_sem_email

print(registro_sem_email(caminho))