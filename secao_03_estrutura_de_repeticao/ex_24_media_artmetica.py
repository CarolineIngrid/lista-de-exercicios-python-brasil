"""
Exercício 24 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o mostre a média aritmética de N notas.

    >>> calcular_media()
    'É necessária ao menos uma nota para calcular a média'
    >>> calcular_media(1)
    1
    >>> calcular_media(1, 3)
    2
    >>> calcular_media(1, 3, 3)
    2.3333333333333335

"""


from statistics import mean


def calcular_media(*notas) -> float:
    """Escreva aqui em baixo a sua solução"""
    
    # if notas == ():
    #     print("'É necessária ao menos uma nota para calcular a média'")
    # else:
    #     soma = 0
    #     for i in notas:
    #         soma +=i
    #     if len(notas) < 2:
    #         print(i)
    #     elif len(notas) == 2:
    #         media = soma/len(notas)
    #         print(f"{media:.0f}")
    #     else:
    #         media = soma/len(notas)
    #         print(media)
    
    if notas == ():
        print("'É necessária ao menos uma nota para calcular a média'")
    else:
        print(mean(notas))
