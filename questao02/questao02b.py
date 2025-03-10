# Construa uma função com dois parâmetros chamados cadeia e padrao. A função
# deve retornar um valor booleano informando se o padrao está contido na cadeia ou
# não.

def padrao_presente(cadeia: str, padrao: str) -> bool:
    return padrao in cadeia

print(padrao_presente('banana','a'))