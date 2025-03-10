#  Construa uma função com os parâmetros ano e sexo. Retorne a quantidade de
# registros com gender igual ao valor do parâmetro sexo e year com o valor maior ou
# igual ao valor do parâmetro ano. Se alguns dos parâmetros não receberem argumentos
# adequados, você deve informar uma mensagem de erro personalizada e retornar
# None.

from questao01a import retorna_lista
import re

caminho = 'dados_usuario.txt'

#funções questões

def retorna_sexo_year(sexo: str, year: str) -> tuple:
    if type(sexo) != str or bool(re.fullmatch(r'[^MFmf]', sexo)) or type(year) != str or not bool(re.fullmatch(r'[0-9]{4}',year)):
        print('Valores Inválidos!')
        return None
    
    registros = retorna_lista(caminho)
    qdt_gender = 0
    qdt_year = 0
    
    for registro in registros: 
        if bool(re.match(sexo.lower(), registro['Gender'].lower())): 
            qdt_gender += 1
            
        if int(year) >= int(registro['Year']): 
            qdt_year += 1

    return qdt_gender, qdt_year


#Testes
qtd_gender, qdt_year = retorna_sexo_year('M','2010')

print(f"A quantidade de sexos iguais são:{qtd_gender}\nA quantidade de ano >= são:{qdt_year}")

