# Questão 2: Gerar Nicknames a Partir de Emails
# Você tem uma lista de dicionários onde cada dicionário contém o nome e o email de uma pessoa. 
# Use map para criar nicknames a partir dos emails. O nickname deve ser a parte do email antes do @, 
# mas convertido para maiúsculas.

from questao06 import retorna_lista 
import re

caminho = 'questao06.csv' 


nicknames = lambda caminho: list(map(lambda item: item["email"].split("@")[0].upper(), retorna_lista(caminho)))

print(nicknames(caminho)) 