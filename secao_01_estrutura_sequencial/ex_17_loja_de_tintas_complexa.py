"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""

import math
def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    area_metros = float(input("Coloque o valor da area em m² aqui: "))
    cobertura = math.ceil((area_metros/6) + (area_metros/6 *0.1)) #quantos litros eu preciso pra pintar certa area

    #tabela preços
    lata_18_preco = 80
    galao_preco = 25
    #litros
    lata_litros = 18
    galao_litros = 3.6

    quant_lata = math.ceil(cobertura/lata_litros) #eu divido quantos litros eu preciso pelo tamanho de litros da lata e essa conta vai me dar quantos litros eu preciso, se for 1,2 vai arrendodar pra duas de uma vez
    quant_galao = math.ceil(cobertura/galao_litros)
    litros_comprados_lata = quant_lata* lata_litros
    litros_comprados_galao = quant_galao*galao_litros

    resto_resto = cobertura % 18
    galaozinho = math.ceil(resto_resto/3.6)
    galaozinho1 = resto_resto/3.6

    #litros_comprados FLOAT

    litros_comprados_galao_float = galaozinho* galao_litros

    soma_preco_galao = quant_galao*galao_preco
    soma_preco = quant_lata*lata_18_preco

    resto_lata = litros_comprados_lata % cobertura 
    resto_galao = litros_comprados_galao % cobertura


    quant_lata_float = cobertura/lata_litros
    quant_lata_floor = math.floor(cobertura/lata_litros)

    
    soma2 = quant_lata_floor*lata_18_preco
    soma3 = galaozinho * galao_preco
    soma_total = soma2 + soma3
    
    total_litros = (quant_lata_floor* lata_litros) +  (galaozinho*galao_litros)
    resto_galao_lata = total_litros - cobertura

    if quant_lata > 0:
        print(f'Você deve comprar {cobertura} litros de tinta.')
        print(f'Você pode comprar {quant_lata} lata(s) de 18 litros a um custo de R$ {soma_preco}. Vão sobrar {resto_lata:.1f} litro(s) de tinta.')
        print(f'Você pode comprar {quant_galao} lata(s) de 3.6 litros a um custo de R$ {soma_preco_galao}. Vão sobrar {resto_galao:.1f} litro(s) de tinta.')

    if resto_resto <= 10.8:
        print(f'Para menor custo, você pode comprar {quant_lata_floor:.0f} lata(s) de 18 litros e {galaozinho} galão(ões) de 3.6 litros a um custo de R$ {soma_total:.0f}. Vão sobrar {resto_galao_lata:.1f} litro(s) de tinta.')


