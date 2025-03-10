# Construa uma função com dois parâmetros chamados cadeia e padrao. A função
# deve retornar a quantidade de vezes que o valor armazenado em padrao aparece no
# conteúdo de cadeia.

def qtd_repeticao(cadeia: str, padrao: str) -> int: 
    return cadeia.count(padrao)

print(qtd_repeticao('banana', 'a'))