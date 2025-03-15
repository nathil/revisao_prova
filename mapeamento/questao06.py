from functools import reduce

lista = [{"nome": "murilo", "media": 9}
         ,{"nome": "carlos", "media":8}
         ,{"nome":"mariazinha", "media": 6}] 


f = lambda soma, item: soma + item["media"] if item["media"] > 7 else soma

def passou(lista):
    lista_passou = []
    cont = 0 
    
    for item in lista:
        if item["media"] > 7: 
            lista_passou.append(item)
            cont += 1
        soma = reduce(f, lista, 0)

    media = soma/cont
    return lista_passou, media

lista_passou, media = passou(lista)

print(f"Alunos que passaram:{lista_passou}\nmedia:{media}")