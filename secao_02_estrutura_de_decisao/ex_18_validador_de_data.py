"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    # if data == '':
    #     print("'Data inválida'")

    novo = data.split('/')

    if len(novo) != 3:
        print("'Data inválida'")
    else:
        dia = int(novo[0])
        mes = int(novo[1])
        ano= int(novo[2])
        if (dia > 31) or (mes > 12) or (ano == 0):
            print("'Data inválida'")
        elif (mes == 2) and (dia > 28):
            print("'Data inválida'")
        else:
            print("'Data válida'")
 