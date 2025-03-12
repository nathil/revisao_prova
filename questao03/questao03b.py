# Considerando a função da questão anterior, cria um laço de repetição que repita
# 1000 vezes. Para cada interação, sorteie dois números entre 1 a 100 e verifique se os
# números sorteados são primos entre si. Crie um arquivo chamado primos_entre_si e,
# para cada sorteio, salve no arquivo os números sorteados e a informação SIM ou NÃO,
# dado o retorno booleano da função da questão anterior. Ao final da execução do
# programa, considerando os 1000 sorteios, você também deve informar a porcentagem
# de números que são primos entre si


import random
from questao03a import primos_entre_si

def retorna_valores_primos():
    
    try:

        with open('primos_entre_si', 'w', encoding='utf-8') as arquivo: 
            arquivo.write('valor_1,valor_2,Primo entre si\n')

        qdt = 0 

        for item in range(1000):
            valor1 = random.randint(1,100)
            valor2 = random.randint(1,100)
            valor_booleano = primos_entre_si(valor1,valor2)

            if primos_entre_si(valor1,valor2) == True: 
                qdt +=1

            registro = f'{valor1},{valor2},{valor_booleano}\n'

            with open('primos_entre_si', 'a', encoding='utf-8') as arquivo: 
                arquivo.write(registro)

        porcen = qdt/10

        print(f'A porcentagem de primos entre si é de:{porcen:.2f}%')
    
    except Exception as e:
        print(f'Inválido! Ocorreu o erro:{e}')

retorna_valores_primos()