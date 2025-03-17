# Questão 15: Filtrar Números Primos em uma Lista de Dicionários
# Você tem uma lista de dicionários onde cada dicionário contém o nome de um aluno e uma lista de 
# números que representam suas notas em diferentes disciplinas. Use filter e uma função personalizada para 
# verificar se um número é primo. Em seguida, crie uma nova lista de dicionários contendo apenas os números 
# primos das notas de cada aluno.

lista = [{'nome': 'jose', 'notas':[10,9,8,9]},
         {'nome': 'marcos', 'notas':[8,7,3,6]}]


def primo(item): 
    if item < 2:
        return False

    for i in range(2,item):
        if item % i == 0: 
            return False
            
    return True

def funcao(lista):
    nova_lista = []

    for item in lista:
        aluno = {"nome": item["nome"], "notas": list(filter(primo, item["notas"]))}
        nova_lista.append(aluno)

    return nova_lista

print(funcao(lista))

        

